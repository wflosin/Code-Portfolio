function results = fixpoint(guess, es)
% f(x) = exp(-x) - x
% 0 = exp(-x) - x
% x = exp(-x)

if nargin < 3
    es = 0.00001;
end

em1 = @(n) exp(-n);
ea = 100;
it = 1;
x = guess;

while es < ea
	it = it + 1;
	x(it) = em1(x(it-1));
	if it > 1
		ea = abs((x(it)-x(it-1))/x(it))*100;
    end
end
results = x(it);
end