"""
following tutorial found here:
https://cloud.dwavesys.com/learning/user/[...]/notebooks/leap/demos/factoring/01-factoring-overview.ipynb

factoring algorithms:
Fermat's algorithm, Pollard's two algorithms, seive algorithms.

between P and NP-hard complexity

factoring is a Constrint Satisfaction problem (csp)

D-wave solves binary quadratic models (BQM), or the CompSci equivalent
quadratic unconstrainedd binary optimization (QUBO) problem.
Maximizes:
sum(i to N)qi*xi + sum(i<j to N)qi,j*xi*xj
qi and qi,j are configurable (linear and quadratic) coefficients
program q so that x also represents solutions to the problem

How to classically minimize:
1)state equation
x+1 = 2
min x[2-(x+1)]**2
factoring:
min a,b[P-ab]**2
    '-> a is represented by a0 + 2a1 + ... + 2**m*am
        where ai is a 0 or 1
2) convert to BQM
reduction techniques for higher terms because terms with a degree > 2
are not solvable by this system
    eg/ xk = a0*b2
    also a0**2 = a0
3) program the quantum computer

"""

### A Simple Light Switch ###
# both switches SW1 and SW2 need to be on for the light to be on
# SW1 ^ SW2 = L
# x1  ^ x2  = x3
# AND gate

import dwavebinarycsp as dbc
import itertools
from dimod import ExactSolver
from dwave.system.samplers import DWaveSampler
from config import ConfigVars as cv
from dwave.embedding import embed_bqm, unembed_sampleset
import minorminer
# Add an AND gate as a constraint to CSP and_csp defined for binary variables 
and_gate = dbc.factories.and_gate(["x1", "x2", "x3"])
and_csp = dbc.ConstraintSatisfactionProblem('BINARY')
and_csp.add_constraint(and_gate)

# Test that for input x1,x2=1,1 the output is x3=1 (both switches on and light shining)
#print(and_csp.check({"x1": 1, "x2": 1, "x3": 1}) == True)

# convert to BQM #
# ^NEED TO LEARN HOW TO^ #
# BQM for an AND gate == 3*x3 + x1*x2 - 2*x1*x3 - 2*x3*x3

# Use itertools to produce all possible 3-bit binary combinations for x1, x2, x3
configurations = []
for (x1,x2,x3) in list(itertools.product([0,1], repeat=3)):
    E = 3*x3+x1*x2-2*x1*x3-2*x2*x3
    configurations.append((E,x1,x2,x3))

#sort from lowest to highest value of the BQM
configurations.sort()
# Print BQM value under "E" and all configurations under "x1, x2, x3"
#all possible combinations of x1,x2,x3 and the BQM value for each
# print("E, x1, x2, x3")
# print(configurations)

# Convert the CSP into BQM and_bqm
and_bqm = dbc.stitch(and_csp)
and_bqm.remove_offset()
# Print the linear and quadratic coefficients. These are the programable inputs to a D-Wave system
# print(and_bqm.linear)
# print(and_bqm.quadratic)

## the BQM values are called "energy"

# Use a dimod test sampler that gives the BQM value for all values of its variables
sampler = ExactSolver()
solution = sampler.sample(and_bqm)
#print(list(solution.data()))

##Factoring on a quantum computer
#1. Express factoring sa a CSP using boolean logic operators
#2. Convert to a BQM
#3. Minimize the BQM

#facoring the number 21
P = 21

# A binary representation of P ("{:06b}" formats for 6-bit binary)
bP = "{:06b}".format(P)
#print(bP)
csp = dbc.factories.multiplication_circuit(3)
# Print one of the CSP's constraints, the gates that constitute 3-bit binary multiplication
#print(next(iter(csp.constraints)))
#Constraint.from_configurations(frozenset({(1, 0, 0), (1, 1, 1), (0, 1, 0), (0, 0, 0)}), ('a0', 'b0', 'p0'), Vartype.BINARY, name='AND(a0, b0) = p0')

#convert to a BQM
bqm = dbc.stitch(csp, min_classical_gap=.1)
# Print a sample coefficient (one of the programable inputs to a D-Wave system)
#print("p0: ", bqm.linear['p0'])

#running a multiplication circuit in reverse
# Our multiplication_circuit() creates these variables
p_vars = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5']

#convert P from decimal to binary
fixed_variables = dict(zip(reversed(p_vars), "{:06b}".format(P)))
fixed_variables = {var: int(x) for(var, x) in fixed_variables.items()}
#{'p5': 0, 'p4': 1, 'p3': 0, 'p2': 1, 'p1': 0, 'p0': 1}

#fix product variables
for var, value in fixed_variables.items():
    bqm.fix_variable(var, value)

# Confirm that a P variable has been removed from the BQM, for example, "p0"
# print("Variable p0 in BQM: ", 'p0' in bqm)
# print("Variable a0 in BQM: ", 'a0' in bqm)

#Submit to the quantum computer
# Use a D-Wave system as the sampler
sampler = DWaveSampler(solver='DW_2000Q_5', token=cv.api_token)
_, target_edgelist, target_adjacency = sampler.structure

#using pre-calculated minor-embedding, turn the graph with the 
#"a0", "b0" netc. nodes into something the QPU can understand
# Set a pre-calculated minor-embeding
#using minorminer, find an embedding
embedding = minorminer.find_embedding(bqm.quadratic, target_edgelist)
if bqm and not embedding:
    raise ValueError("no embedding found")

# Apply the embedding to the factoring problem to map it to the QPU
bqm_embedded = embed_bqm(bqm, embedding, target_adjacency, 3.0)

# Confirm mapping of variables from a0, b0, etc to indexed qubits 
# print("Variable a0 in embedded BQM: ", 'a0' in bqm_embedded)
# print("First five nodes in QPU graph: ", sampler.structure.nodelist[:5])
# Variable a0 in embedded BQM:  False
# First five nodes in QPU graph:  [0, 1, 2, 3, 4]

# Request num_reads samples - how many samples the QPU runs
kwargs = {}
if 'num_reads' in sampler.parameters:
    kwargs['num_reads'] = 100
if 'answer_mode' in sampler.parameters:
    kwargs['answer_mode'] = 'histogram'
response = sampler.sample(bqm_embedded, **kwargs)
#print("A solution indexed by qubits: \n", next(response.data(fields=['sample'])))
#A solution indexed by qubits: Sample(sample={1617: 0, 1622: 1, 1624: 1, 1625: 1, 1630: 1, 1631: 1, 1633: 1, 1634: 1, 1638: 1, 1639: 1, 1640: 1, 1646: 1, 1745: 0, 1752: 1, 1753: 1, 1754: 1, 1755: 0, 1756: 0, 1757: 1, 1759: 1, 1760: 1, 1761: 0, 1762: 1, 1763: 1, 1764: 0, 1765: 1, 1766: 1, 1767: 1, 1768: 1, 1769: 0, 1770: 1, 1771: 1, 1772: 0, 1774: 1, 1775: 1, 1872: 0, 1873: 0, 1876: 1, 1877: 0, 1878: 0, 1880: 1, 1881: 1, 1882: 1, 1883: 0, 1884: 1, 1885: 0, 1886: 0, 1887: 1, 1888: 1, 1889: 0, 1890: 1, 1891: 1, 1892: 1, 1893: 1, 1894: 0, 1895: 1, 1896: 1, 1897: 0, 1898: 1, 1899: 1, 1900: 1, 1901: 1, 1902: 0, 1903: 1, 2001: 0, 2007: 0, 2008: 1, 2010: 0, 2011: 0, 2012: 0, 2015: 0, 2018: 1, 2019: 1, 2020: 0, 2023: 0, 2024: 0, 2025: 0, 2026: 0, 2028: 0, 2031: 0})

# Map back to the BQM's graph (nodes labeled "a0", "b0" etc,)
response = unembed_sampleset(response, embedding, source_bqm=bqm)
#print("\nThe solution in problem variables: \n",next(response.data(fields=['sample'])))
# The solution in problem variables: Sample(sample={'a0': 1, 'a1': 1, 'a2': 0, 'and0,1': 1, 'and0,2': 1, 'and1,0': 1, 'and1,1': 1, 'and1,2': 1, 'and2,0': 0, 'and2,1': 0, 'and2,2': 0, 'b0': 1, 'b1': 1, 'b2': 1, 'carry1,0': 1, 'carry1,1': 1, 'carry2,0': 0, 'carry2,1': 1, 'carry3,0': 0, 'sum1,1': 0, 'sum2,1': 0})

#large_sample = response.samples(n=25)


# results = []
# for sample in list(response.samples(n=10)):
#     dict(sample)
#     #print(sample)
#     #turn into decimal 
#     a = int(str(sample['a2'])+str(sample['a1'])+str(sample['a0']),2)
#     b = int(str(sample['b2'])+str(sample['b1'])+str(sample['b1']),2)
#     results.append([a,b])
# print(results)

#Select just just the first sample. 
sample = next(response.samples(n=1))
dict(sample)
print(sample)
a = int(str(sample['a2'])+str(sample['a1'])+str(sample['a0']),2)
b = int(str(sample['b2'])+str(sample['b1'])+str(sample['b0']),2)
print("Given integer P={}, found factors a={} and b={}".format(P, a, b))


