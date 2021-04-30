# same solution but shiftAndUpdate is written better

# O(N) Time | #O(1) space
def findThreeLargestNumbers(array):
    # fixed size array
	# input array always greater than 3
	max_vals = [None, None, None]

	# for loop saving max1 max2 max3, where max1 <= max2 <= max3
	# should also save if comparng to None
	for element in array:
		#print('{} {}'.format(max_vals, element))
		updateLargest(max_vals, element)
	
	return max_vals

def updateLargest(max_vals, insertNum):
	if max_vals[2] is None or insertNum > max_vals[2]:
		# shift and update 2
		shiftAndUpdate(max_vals, insertNum, 2)
	elif max_vals[1] is None or insertNum > max_vals[1]:
		# shift and update 2
		shiftAndUpdate(max_vals, insertNum, 1)
	elif max_vals[0] is None or insertNum > max_vals[0]:
		# shift and update 0
		shiftAndUpdate(max_vals, insertNum, 0)

def shiftAndUpdate(array, insertNum, idx):
	for i in range(idx + 1):
		if i == idx:
			array[i] = insertNum
		else:
			array[i] = array[i+1]