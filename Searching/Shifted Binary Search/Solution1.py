'''
Sorted but shifted array
Apply some variation of binary search on the array
Compare number above left pointer to number above middle pointer.
if val < M AND val >= L, explore left
else explore right
'''

# O(logn) ST
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	potMatch = array[middle]
	leftNum = array[left]
	rightNum = array[right]
	if target == potMatch:
		return middle
	elif leftNum <= potMatch:
		if target < potMatch and target >= leftNum:
			return shiftedBinarySearchHelper(array, target, left, middle - 1)
		else:
			return shiftedBinarySearchHelper(array, target, middle + 1, right)
	else:
		if target > potMatch and target <= rightNum:
			return shiftedBinarySearchHelper(array, target, middle + 1, right)
		else:
			return shiftedBinarySearchHelper(array, target, left, middle - 1)