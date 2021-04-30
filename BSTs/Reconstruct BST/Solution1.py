# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) T | O(n) S
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
		return None
	
	currentValue  =preOrderTraversalValues[0]
	rightSubtreeRootIdx = len(preOrderTraversalValues)
	
	for idx in range(1, len(preOrderTraversalValues)):
		value = preOrderTraversalValues[idx]
		if value >= currentValue:
			rightSubtreeRootIdx = idx
			break
			
	leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
	rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
	
	return BST(currentValue, leftSubtree, rightSubtree)