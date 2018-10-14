function [results] = golden(xu,xl,es)
if nargin < 3
	es = 0.0000001;
end

if xl > xu
	error('Invalid input')
end

syms x
func(x) = 2*sin(x)-(x^2)/10;
gold = (sqrt(5)-1)/2;
ea = 100;
i = 0;

while ea > es
	i = i + 1;
	xr = gold*(xu - xl);
	x1 = xl + xr;
	x2 = xu - xr;
	if func(x1) > func(x2)
		xl = x2;
		xopt = x1;
    elseif func(x1) < func(x2)
		xu = x1;
		xopt = x2;
	end

	if i > 1
		ea = (1-gold) * abs((xu - xl)/xopt) * 100;
    end
end
results = xopt;
end