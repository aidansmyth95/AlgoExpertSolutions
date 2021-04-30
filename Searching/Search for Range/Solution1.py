'''
Return array of length 2, range for where you can find a target element.
Array is sorted.
Binary search variation
Three pointers, L, M, R
Since array is sorted, if number to left is not same number, we would have
reached left extremity. Similar for right.
Recursive and iterative solutions as usual
'''

# O(log(n)) ST
def searchForRange(array, target):
    finalRange = [-1, -1]
	alteredBinarySearch(array, target, 0, len(array), finalRange, True)
	alteredBinarySearch(array, target, 0, len(array), finalRange, False)
	return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
	if left > right:
		return
	mid = (left + right) // 2
	if array[mid] < target:
		# go right
		alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
	elif array[mid] > target:
		# go left
		alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
	else:
		if goLeft:
			if mid == 0 or array[mid - 1] != target:
				# if at leftmost extremety
				finalRange[0] = mid
			else:
				# go left
				alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
		else:
			if mid == len(array) - 1 or array[mid + 1] != target:
				# if at rightmost extremety
				finalRange[1] = mid
			else:
				# go right
				alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)