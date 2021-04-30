# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, numVisited, latestValue):
		self.numVisited = numVisited
		self.latestValue = latestValue

# O(h + k) T | O(h) S
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
	reverseInOrderTraverse(tree, k, treeInfo)
	return treeInfo.latestValue

def reverseInOrderTraverse(node, k, treeInfo):
	if node is None or treeInfo.numVisited >= k:
		return
	
	reverseInOrderTraverse(node.right, k, treeInfo)
	if treeInfo.numVisited < k:
		treeInfo.numVisited += 1
		treeInfo.latestValue = node.value
		reverseInOrderTraverse(node.left, k, treeInfo)
