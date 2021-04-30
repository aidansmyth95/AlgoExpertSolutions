'''
All elements are at most k away from their sorted solution. k < n

Me: I would do a sliding window approach. Likely time complexity would be too
great though. Would be O(nk) T, which is sub-optimal.

At any time all we need to do is look at k+1 elements away from current idx

Better approach: min heap to improve time complexity. All children must be
greater than parent. Root is minimum element.

To add/remove root from heap is O(log(n))T, to initialize heap is O(n)T.

We are going to sort in place to save space complexity.

'''

# O(nlogk + k) -> O(nlog(k)) T | O(k) S
def sortKSortedArray(array, k):
    minHeap = MinHeap(array[:min(k + 1, len(array))])
	sortedIdx = 0
	for idx in range(k + 1, len(array)):
		# pull element from min heap
		minElement = minHeap.remove()
		# place it at sorted idx
		array[sortedIdx] = minElement
		sortedIdx += 1
		# insert new element in min heap and repeat
		currentElement = array[idx]
		minHeap.insert(currentElement)
	
	# there will be k elements left to handle at the end
	# perform same thing, only we don't need to add anything to heap.
	while not minHeap.isEmpty():
		minElement = minHeap.remove()
		array[sortedIdx] = minElement
		sortedIdx += 1

	return array
		
class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)
		
	def isEmpty(self):
		return len(self.heap) == 0
	
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			tmpIdx = currentIdx * 2 + 2
			childTwoIdx = tmpIdx if tmpIdx <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
	
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
			
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
		
	def swap(self, i, j, heap):
		heap[i] , heap[j] = heap[j] , heap[i]
