'''
This soltion is iterative and has O(1) S
'''

# O(logn) T | O(1) S
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
	while left <= right:
		middle = (left + right) // 2
		potMatch = array[middle]
		leftNum = array[left]
		rightNum = array[right]
		if target == potMatch:
			return middle
		elif leftNum <= potMatch:
			if target < potMatch and target >= leftNum:
				right= middle - 1
			else:
				left = middle + 1
		else:
			if target > potMatch and target <= rightNum:
				left = middle + 1
			else:
				right= middle - 1
	return -1