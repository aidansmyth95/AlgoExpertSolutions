'''
Start with empty sorted array.

Make unsorted sublist (a max heap) smaller, and sorted sublist bigger
1. Transform unsorted array into max heap
2. Grap max val and swap to end
3. Sift down to get new max val in unsorted sublist
4. Swap with one from end and repeat...
'''

# O(nlogn) T - n sift downs
# O(1) S - everything inplace, just swaps used
def heapSort(array):
    buildMaxHeap(array)
	for endIdx in reversed(range(1, len(array))):
		swap(0, endIdx, array)
		siftDown(0, endIdx - 1, array)
	return array

def buildMaxHeap(array):
	firstParentIdx = (len(array) - 2) // 2
	for currentIdx in reversed(range(firstParentIdx + 1)):
		siftDown(currentIdx, len(array) - 1, array)
	return array

def siftDown(currentIdx, endIdx, heap):
	childOneIdx = currentIdx * 2 + 1
	while childOneIdx <= endIdx:
		tmp = currentIdx * 2 + 2
		childTwoIdx = tmp if tmp <= endIdx else -1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(currentIdx, idxToSwap, heap)
			currentIdx = idxToSwap
			childOneIdx = currentIdx * 2 + 1
		else:
			return

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
