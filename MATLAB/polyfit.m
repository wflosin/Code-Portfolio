function [coefficients] = poly_fit(fit_data, ord)
	%fit_data= 
	%[0,2;
	% 1,10;
	% 2,28;
	% 3,56;
	% 4,94;
	% 5,142]


	x_val = fit_data(:,1);
	y_val = fit_data(:,2);

	[row, column] = size(fit_data);

%This initializes the x matrix
 for row_i = 1:ord+1
 	for column_j = 1:ord+1
 		%initialize the matrix location to prevent index out of range
 		V(row_i, column_j) = 0;
 		for index = 1:row
 			%Matrix = matrix + x^(i-1)
 			V(row_i, column_j) = V(row_i, column_j) + x_val(index)^((column_j-1)+(row_i-1));
 		end
 	end
end

%This initializes the y vector
for row_i = 1:ord+1
	%initialize the matrix location to prevent index out of range
	y(row_i)=0;
	for index = 1:row
		y(row_i) = y(row_i) + y_val(index) * x_val(index)^(row_i-1);
	end
end

% Main equation:
% V^-1 * V * coefficients = V^-1 * y
disp(V)
disp(y)
pause
coefficients = inv(V) * y';