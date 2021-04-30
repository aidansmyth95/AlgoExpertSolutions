'''
Return array of length 2, range for where you can find a target element.
Array is sorted.
Binary search variation
Three pointers, L, M, R
Since array is sorted, if number to left is not same number, we would have
reached left extremity. Similar for right.
Recursive and iterative solutions as usual
'''

# O(log(n)) T | O(1) S
def searchForRange(array, target):
    finalRange = [-1, -1]
	alteredBinarySearch(array, target, 0, len(array), finalRange, True)
	alteredBinarySearch(array, target, 0, len(array), finalRange, False)
	return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
	while left <= right:
		mid = (left + right) // 2
		if array[mid] < target:
			# go right
			left = mid + 1
		elif array[mid] > target:
			# go left
			right = mid - 1
		else:
			if goLeft:
				if mid == 0 or array[mid - 1] != target:
					# if at leftmost extremety
					finalRange[0] = mid
					return
				else:
					# go left
					right = mid - 1
			else:
				if mid == len(array) - 1 or array[mid + 1] != target:
					# if at rightmost extremety
					finalRange[1] = mid
					return
				else:
					# go right
					left = mid + 1
