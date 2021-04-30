'''
First value is pivot.
Left pointer and right pointer
Is left number greater than pivot number and right number is smaller than pivot,
swap left and right.
Once left is greater than right, swap pivot with right pointer.
Right pointer in this case will always be smaller than pivot
'''

# Best case: O(nlog(n)) ST - when pivot divides array in half, similar to
# binary search as you would be splitting in half array each time.
# Avg case: Same as best case, complex maths explanation for it.
# Space: when calling on smallest subarray, at most this many recursive calls.
# Worst case: O(n^2) T
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	# outside of while loop
	swap(pivotIdx, rightIdx, array)
	# call first on smaller subarray
	leftSubArrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubArrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)
		
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
