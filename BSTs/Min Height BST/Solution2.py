'''
A recursive implementation with lower O(N) T complexity.
'''

def minHeightBst(array):
	return constructMinHeightBstHelper(array, None, 0, len(array) - 1)

# O(n) T -> n nodes and no insert method | O(N) S
def constructMinHeightBstHelper(array, bst, startIdx, endIdx):

	if endIdx < startIdx:
		return

	midIdx = (startIdx + endIdx) // 2
	newBstNode = BST(array[midIdx])
	
	if bst is None:
		bst = newBstNode
	else:
		# so this time we do not want to use insert
		# let us change right or left node value instead
		if array[midIdx] < bst.value:
			# place to left if < node value
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
			
	# and recursively call on subarrays as before
	constructMinHeightBstHelper(array, bst, startIdx, midIdx - 1)
	constructMinHeightBstHelper(array, bst, midIdx + 1, endIdx)
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	# haha, we don't need you anymore!
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
