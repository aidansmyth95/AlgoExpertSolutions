# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) ST
def findKthLargestValueInBst(tree, k):
    sortedValues = []
	inOrderTraverse(tree, sortedValues)
	return sortedValues[-k]

def inOrderTraverse(node, sortedValues):
	if node is None:
		return
	
	inOrderTraverse(node.left, sortedValues)
	sortedValues.append(node.value)
	inOrderTraverse(node.right, sortedValues)
