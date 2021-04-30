'''
If one unsorted number, then there exists at least one other out of place number
Smallest and greatest unsorted numbers dictate subarray to sort size
'''


# O(n) T | O(1) S
def subarraySort(array):
    smallestUnsorted = float("inf")
	biggestUnsorted = float("-inf")
	
	# iterate through array, marking unsorted as we go
	for i in range(len(array)):
		if isUnsorted(i, array):
			smallestUnsorted = min(smallestUnsorted, array[i])
			biggestUnsorted = max(biggestUnsorted, array[i])
	# check if array does not need to be sorted
	if smallestUnsorted == float("inf"):
		return [-1, -1]

	# after for loop, we have max and min unsorted values. Find their sorted idx
	leftIdx = 0
	rightIdx = len(array) - 1
	# to while loops to move both idx. We want them to move the extra step 
	# inwards if equal, to minimize subarray size
	while smallestUnsorted >= array[leftIdx]:
		leftIdx += 1
	while biggestUnsorted <= array[rightIdx]:
		rightIdx -= 1	
	return [leftIdx, rightIdx]
	
def isUnsorted(i, array):
	# corner cases
	if len(array) < 2:
		return False
	if i == 0:
		return array[i] > array[i+1]
	if i == len(array) - 1:
		return array[i] < array[i-1]
	# when not at extremity
	return array[i-1] > array[i] or array[i+1] < array[i]
