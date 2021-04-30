'''
Sorted array as input. Non-repeating integers.
Return index of first occurence when idx is equal to value at idx
Return -1 if no such case
Brute force solution runs in O(n) T. We can do better. Binary search.
Could do recursively or iteratively
'''

# Recursive Soln
# O(log(n)) ST
def indexEqualsValue(array):
    return indexEqualsValueHelper(array, 0, len(array) - 1)
	
def indexEqualsValueHelper(array, leftIdx, rightIdx):
	if leftIdx > rightIdx:
		return -1
	
	midIdx = leftIdx + (rightIdx - leftIdx) // 2
	midVal = array[midIdx]
	
	if midVal < midIdx:
		# if idx is greater than val, all vals to left will be greater
		# than their idx, so go to right
		return indexEqualsValueHelper(array, midIdx + 1, rightIdx)
	elif midVal == midIdx and midIdx == 0:
		# if first element no need to check before it
		return midIdx
	elif midVal == midIdx and array[midIdx - 1] < midIdx - 1:
		# no more equality in previous example, so we can return
		return midIdx
	else:
		# look to left
		return indexEqualsValueHelper(array, leftIdx, midIdx - 1)
	
	return -1
