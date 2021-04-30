def binarySearch(array, target):
    # array is already sorted
	return binarySearchHelper(array, target, 0, len(array)-1)

'''
Pro tip: if an array is sorted, it will often indicate that
binary search is the solution.

Sub-optimal version - recursion
'''

# O(log(n)) time | O(log(n)) space
def binarySearchHelper(array, target, left_idx, right_idx):
	# this method will move the left and right idx until overlap
	if left_idx > right_idx:
		# we are done if they meet
		return -1
	
	middle_idx = (left_idx + right_idx) // 2
	checkVal = array[middle_idx]
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
	#print('{} {}'.format(left_idx, right_idx))
	return binarySearchHelper(array, target, left_idx, right_idx)
