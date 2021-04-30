def binarySearch(array, target):
    # array is already sorted
	return binarySearchHelper(array, target, 0, len(array)-1)

'''
Can we do better in space? Yes if we go iteratively.
Optimal version - iteratively
Only one function call on stack
'''

# O(log(n)) time | O(1) space
def binarySearchHelper(array, target, left_idx, right_idx):
	# this method will move the left and right idx until overlap
	while left_idx <= right_idx:
		middle_idx = (left_idx + right_idx) // 2
		checkVal = array[middle_idx]
		#print('{} {} {}'.format(checkVal, left_idx, right_idx))
		if checkVal == target:
			print(middle_idx)
			return middle_idx
		elif target < checkVal:
			# right upper limit is now set to middle idx
			right_idx = middle_idx -1
		else:
			# target < checkVal
			# left lower limit is now set to middle idx
			left_idx = middle_idx + 1
	# we are done if they meet
	return -1
