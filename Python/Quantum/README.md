Q_factoring.py

*Most of this code is from the D-Wave Online Learning Platform, it does not belong to me, but I 
used it to learn*

This script utilizes D-Wave's quantum computer (QPU) and the API used to access it to factor 
a number between zero and 49.  The code builds a Constraint Satisfaction Problem and turns it 
into Boundary Constrain Problem, to then be solved in the quantum computer. The logic gate 
outlined for the QPU to optimize is a 3-bit multiplier.  The system takes in what would normally 
be the 6-bit output, and runs 100 samples on the QPU, to then return the result of the 
computation to the user; two factors of the number given (which is set to be 21).
ss
The code requires access to a D-Wave Leap account to access the QPU, so the API token was omitted.
