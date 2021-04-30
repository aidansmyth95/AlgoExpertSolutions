'''
Sorted array as input. Non-repeating integers.
Return index of first occurence when idx is equal to value at idx
Return -1 if no such case
Brute force solution runs in O(n) T. We can do better. Binary search.
Could do recursively or iteratively
'''

# Recursive Soln
# O(log(n)) T | O(1) S
def indexEqualsValue(array):

	leftIdx = 0
	rightIdx = len(array) - 1
	
	while leftIdx <= rightIdx:
	
		midIdx = leftIdx + (rightIdx - leftIdx) // 2
		midVal = array[midIdx]

		if midVal < midIdx:
			# if idx is greater than val, all vals to left will be greater
			# than their idx, so go to right
			leftIdx = midIdx + 1
		elif midVal == midIdx and midIdx == 0:
			# if first element no need to check before it
			return midIdx
		elif midVal == midIdx and array[midIdx - 1] < midIdx - 1:
			# no more equality in previous example, so we can return
			return midIdx
		else:
			# look to left
			rightIdx = midIdx - 1
	
	return -1
