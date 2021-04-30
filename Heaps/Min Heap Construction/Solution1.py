'''
Heap is a BST, but must have all levels filled completely, except from last
one which is filled from left to right.
In no way sorted. All nodes smaller than children nodes.
Can be represented as lists. Root node at index 0.
Children nodes are (2i + 1) and (2i + 2).
Parent node floor((i-1)/2).

Build heap: Takes array that is not a heap, and builds a min heap or max heap.
			Call sift down on every parent node in heap. Positions every
			parent node correctly. STart at last parent node.
Insert: Add to be last node in heap. Then sift it up to its correct position.
		Continuously swap until in correct position.
Remove: swap node to remove with last node, then pop. The sift down to place
		swapped node in its correct position. We are comparing it to both
		its children nodes. Take smallest value of children and swap.
'''

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# O(N) T | O(1) S - sure we have N sift downs, but it runs different on
	# on every node. Leaf nodes and some nodes go down different levels.
	# The higher up you are, the longer it takes to run. The very bottom
	# nodes are O(0). Balances out to O(N) T if we use Taylor series.
    def buildHeap(self, array):
		self.heap = array
		firstParentIdx = (len(self.heap) - 2) // 2
		for idx in reversed(range(firstParentIdx + 1)):
			self.siftDown(idx, len(self.heap) - 1)
		return self.heap

	# O(logN) T | O(1) S
    def siftDown(self, currentIdx, endIdx):
		# we need to compare to both child nodes
		childOneIdx = 2 * currentIdx + 1
		while childOneIdx <= endIdx:
			# as soon as we do not have a child node, we are done
			# check if there is a child 2
			childTwoIdx = 2 * currentIdx + 2 if 2 * currentIdx + 2 <= endIdx else -1
			if childTwoIdx != -1 and self.heap[childTwoIdx] < self.heap[childOneIdx]:
				# decide which child to swap with parent
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if self.heap[idxToSwap] < self.heap[currentIdx]:
				# compare to parent node
				self.swap(currentIdx, idxToSwap, self.heap)
				currentIdx = idxToSwap
				childOneIdx = 2 * currentIdx + 1
			else:
				return
						
	# O(logN) T | O(1) S
    def siftUp(self, currentIdx):
		# modify self.heap which is an array
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and self.heap[currentIdx] < self.heap[parentIdx]:
			# while we are not at root and can sift up / swap nodes
			self.swap(currentIdx, parentIdx, self.heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

	# O(1) ST
    def peek(self):
        return self.heap[0]

	# O(logN) T | O(1) S
    def remove(self):
        # swap root with last value, pop new root, and sift down
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1)
		return valueToRemove

	# O(logN) T | O(1) S
    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1)
	
	@staticmethod
	def swap(i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
