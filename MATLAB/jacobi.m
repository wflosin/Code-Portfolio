function [ x ] = jacobi(A, b , guess, es)
% A is the inputted matrix
% b is the column vector
% guess is the x initial x column vector in the equation [A][x] = [b]
% es is the strop criterion/ tolerance using %relative error . Default: 0.00001

% if only three inputs
if nargin < 4
	es = 0.00001;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Checks if the matrix is a square
[R, C] = size(A);
if R ~= C
	error('The inputted matrix needs to be square');
end

% Chack if guess is the same size as b
if (size(b) ~= size(guess)) | size(b,2) ~= 1 | size(guess,2) ~= 1
	error('The inputted column vector or initial guess is not the correct size');
end

% Check if b or guess is the same size as a column of A
if size(b,1) ~= C | size(guess,1) ~= C
	error('The inputted column vector or initial guess does not match the column length of the minputted matrix')
end

% Check if diagonally dominant (the diagonal is larger than the sum of the row entries)
for r = 1:R
	rowvec = abs(A(r,:));
	if rowvec(r) < (sum(rowvec) - rowvec(r))
		error('The inputted matrix is not diagonally dominant');
	end 
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial guess
x = guess;

% Will make an empty matrix but with the diagonal vlaues of A as the diagonal
diagonal = diag(diag(A));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% x1 = (1/a11)*(b1 - (a12*x2 + a13*x3))
%-> xi+1 = diag(A)^-1 * {b - (A-diag(A))*xi}

% Jacobi Iteration Method
erro_r = inf;
while erro_r > es
	d_x = diagonal\(b - A*x);
	x = x + d_x;

	erro_r = max(abs(d_x./x));
end