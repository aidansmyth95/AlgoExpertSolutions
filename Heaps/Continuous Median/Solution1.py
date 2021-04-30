'''
Receive continuous stream of numbers and retrieve median at any time.
This problem will use heaps.

Insertion/removal in a heap only takes log(n) time, excluding heap balancing.
Quicker than array insert.

After insertion, we will want to check if we need to rebalance heap. Based
on their lengths. Remove/insert elements.

Insertion sort is the trivial, sub-optimial way to do it.

We only care about keeping track of two buckets: greater half and lower half.
Access their max and min and count, we can get median.
'''

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		# max heap
		self.lowers = Heap(MAX_HEAP_FUNC, [])
		# min heap
		self.greaters = Heap(MIN_HEAP_FUNC, [])

	# O(logn) T | O(n) S
    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
			self.lowers.insert(number)
		else:
			self.greaters.insert(number)
		self.rebalanceHeaps()
		self.updateMedian()
	
	def rebalanceHeaps(self):
    	if self.lowers.length - self.greaters.length == 2:
			self.greaters.insert(self.lowers.remove())
		elif self.greaters.length - self.lowers.length == 2:
			self.lowers.insert(self.greaters.remove())
			
	def updateMedian(self):
		if self.lowers.length == self.greaters.length:
			self.median = (self.lowers.peek() + self.greaters.peek()) / 2
		elif self.lowers.length > self.greaters.length:
			self.median = self.lowers.peek()
		else:
			self.median = self.greaters.peek()
			
			
	def getMedian(self):
        return self.median

class Heap:
	def __init__(self, comparisonFunc, array):
		self.comparisonFunc = comparisonFunc
		self.heap = self.buildHeap(array)
		self.length = len(self.heap)
		
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			tmp_idx = currentIdx * 2 + 2
			childTwoIdx = tmp_idx if tmp_idx <=endIdx else -1
			if childTwoIdx != -1:
				if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
					idxToSwap = childTwoIdx
				else:
					idxToSwap = childOneIdx
			else:
				idxToSwap = childOneIdx
			if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
	
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0:
			if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
				self.swap(currentIdx, parentIdx, heap)
				currentIdx = parentIdx
				parentIdx = (currentIdx - 1) // 2
			else:
				return
	
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		self.swap(0, self.length-1, self.heap)
		valueToRemove = self.heap.pop()
		self.length -= 1
		self.siftDown(0, self.length - 1, self.heap)
		return valueToRemove
	
	def insert(self, value):
		self.heap.append(value)
		self.length += 1
		self.siftUp(self.length - 1, self.heap)
		
	def swap(self, i, j, array):
		array[i], array[j] = array[j], array[i]
		
def MAX_HEAP_FUNC(a, b):
	return a > b

def MIN_HEAP_FUNC(a, b):
	return a < b