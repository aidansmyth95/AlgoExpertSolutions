'''
Very similar to quicksort.
When pivot is swapped, we decide which subtree to look at next
When pivot is swapped, if it is at k, we have answer.
'''

# Time complexities below:
# Worst O(n^2) - divide array in 1 size 1 and 1 huge subarray every time
# Best O(n) - Divides array in half. Geometric series -> converges to 2N -> N
# Avg O(n) - Trickier to prove, but similar idea.
def quickselect(array, k):
    pos = k - 1
	return quickSelectHelper(array, 0, len(array) - 1, pos)
	
def quickSelectHelper(array, startIdx, endIdx, pos):
	while True:
		if startIdx > endIdx:
			raise Exception
		pivotIdx = startIdx
		leftIdx = startIdx + 1
		rightIdx = endIdx
		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
				swap(leftIdx, rightIdx, array)
			if array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			if array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1
		swap(pivotIdx, rightIdx, array)
		if rightIdx == pos:
			return array[rightIdx]
		elif rightIdx < pos:
			# go right
			startIdx = rightIdx + 1
		else:
			# go left
			endIdx = rightIdx - 1
				
				
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
			
