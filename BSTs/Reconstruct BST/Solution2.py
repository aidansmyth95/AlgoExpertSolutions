# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, rootIdx):
		self.rootIdx = rootIdx

# O(n) ST
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
	return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	
	currentSubtreeInfo.rootIdx += 1
	leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
	rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
	return BST(rootValue, leftSubtree, rightSubtree)
	