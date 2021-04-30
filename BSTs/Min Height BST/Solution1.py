'''
Recursive implementation. A little worse than the others, as it uses
BST insert O(logN) per node

Note: if repeated numbers, answer would be very different. We would not be
using midIdx naively.
'''
def minHeightBst(array):
	return constructMinHeightBstHelper(array, None, 0, len(array) - 1)

# O(nlog(n)) T -> n nodes and log(n) insert for each node | O(N) S -> we store N nodes in memory)
def constructMinHeightBstHelper(array, bst, startIdx, endIdx):

	if endIdx < startIdx:
		return

	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]

	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)

	# then start again with left sub-array
	constructMinHeightBstHelper(array, bst, startIdx, midIdx - 1)
	# then start again with right sub-array
	constructMinHeightBstHelper(array, bst, midIdx + 1, endIdx)
	
	return bst
	

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	# this is O(log(N)) per node insert
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
