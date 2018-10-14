function [du] = richardson22( D, u, x, h, N_max, eps_abs )
% richardson22
% Copy the description from 2.1 here
%
% Parameters
% ==========
%    D      The function D takes a function u and two real-values, x and h, 
%            and return an approximation of the derivative of the function u 
%            using the centered divided-difference formula
%    u      The function handle u approximates u at x and step size h
%
%    x      The value corresponding to the point on the x-axis where we want   
%            to solve for the derivative
%    h      The step size from x
%
%    N_max  The maximum amount of iterations possible
%    eps_abs    The strop criterion/ tolerance using % relative error
%
% Return Value
% ============
%    du     The approximation for the given function u at point x
 
if ~isa(D,'function_handle')
    throw( MException('MATLAB:invalid_argument', ...
        'The argument D is not a function handle'))
end
 
if ~isa(u,'function_handle')
    throw( MException('MATLAB:invalid_argument', ...
        'The argument u is not a function handle'))
end
 
if ~isscalar(x)
    throw( MException('MATLAB:invalid_argument', ...
        'The argument x is not a scalar'))
end
 
if ~isscalar(h)
    throw( MException('MATLAB:invalid_argument', ...
        'The argument h is not a scalar'))
end
 
if ~isscalar(N_max) || (N_max <= 0)
    throw( MException('MATLAB:invalid_argument', ...
        'The argument N_max is not a positive scalar'))
end
 
if ~isscalar(eps_abs) || (eps_abs <= 0)
    throw( MException('MATLAB:invalid_argument', ...
        'The argument eps_abs is not a positive scalar'))
end
%----------------------------------------------------------%
%a matrix to store the iterated approximations
R = zeros(N_max);
 
%two loops that fill in the matrix R in a lower triangular pattern
for m = 1:N_max
    for n = 1:m
        %If n equals to 1, or if the iteration is in the first column, %solve for R(m,1)
        if n == 1
            R(m,n) = D(u, x, h/2^(m-1));
 
        %Otherwise, solve using the weighted average of two indices  %R(m,n-1) and R(m-1,n-1)
        else
            R(m,n) = (4^(n-1) * R(m,n-1) - R(m-1,n-1))/(4^(n-1) -1);
        end
 
        %check if the difference in approximations between the current %iteration and the iteration prior is within the tolerance range, 
        %as well that n and m are equal and n (and m) don’t equal 1, and %return R(m,n)
        %I included commented out outputs of the absolue and relative error
        if n == m && n ~= 1 && abs(R(m,n) - R(m-1,n-1)) < eps_abs
            %abs_error = abs(R(m,n) - R(m-1,n-1))
            %rel_error = abs(R(m,n) - R(m-1,n-1)/R(m,n))
            du = R(m,n);
            return 
        end
    end     
end
 
%If the loops break without returning any values, throw and exception saying %that the Richardson extrapolation did not converge
throw( MException('MATLAB:Function_failed', 'The Richardson extrapolation did not converge'))
 
end

