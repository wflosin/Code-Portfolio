function [ array1 ] = sorting( array1 )
%selection sort

	sorted = 0;

	for i = 1:length(array1)
		for j = 1:length(array1)
			if array1(j) > array1(i)
				index1 = array1(j);
				array1(j) = array1(i);
				array1(i) = index1;
			end
		end
    end
    if sorted == check_sorted(array1)
        disp(array1)
    end