
# O(N) Time | #O(1) space
def findThreeLargestNumbers(array):
    # fixed size array
	# input array always greater than 3
	max_vals = [None, None, None]

	# for loop saving max1 max2 max3, where max1 <= max2 <= max3
	# should also save if comparng to None
	for element in array:
		#print('{} {}'.format(max_vals, element))
		if max_vals[2] is None or element > max_vals[2]:
			# shift back 2
			max_vals[0] = max_vals[1]
			max_vals[1] = max_vals[2]
			max_vals[2] = element
		elif max_vals[1] is None or element > max_vals[1]:
			# shift back 1
			max_vals[0] = max_vals[1]
			max_vals[1] = element
		elif max_vals[0] is None or element > max_vals[0]:
			max_vals[0] = element
	
	return max_vals