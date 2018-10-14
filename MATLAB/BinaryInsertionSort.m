function [ temp_array ] = sorting( array1 )
%This is based off of Python's "sorted" function or Timsort,
%adapted from c++ to MATLAB
%This is just the binary search portion of the whole Timsort

sorted = 0;
temp_array = [array1(1)];

for i = 1:length(array1)
    %disp(i)
	item = temp_array(end);
	left = 1;
	right = i;
    midpoint = 0;
	while left < right
		midpoint = floor((left + right)/ 2);
		if temp_array(midpoint) < item
	    	left = midpoint + 1;        
	    else
	    	right = midpoint - 1;
	    end
	end
	if length(array1) > 2
		if midpoint ~= i-1
			run1 = [temp_array(1:midpoint) temp_array(end) temp_array(midpoint+1:end-1)];
		else
			run1 = temp_array;
		end	
    end
    if i ~= length(temp_array)
        disp(temp_array)
        temp_array = [temp_array(1:end) array1(i+1)];
    end
end

