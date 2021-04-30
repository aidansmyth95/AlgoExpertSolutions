"""
Every node should be <= all nodes to the right
Kep checking children values recursively.
Validate all sub-trees
If tree is None, we are done. Return True.
Every value has a minimum and maximum value range to be valid.
minVal <= node < maxVal
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# O(N)T (we check every node) | O(d)
def validateBst(tree):
	return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minVal, maxVal):
	# bottom of branch
	if tree is None:
		return True

	# invalid node value check
	if tree.value < minVal or tree.value >= maxVal:
		return False

	# left-subtree: update maxVal is value of current node
	leftIsValid = validateBstHelper(tree.left, minVal, tree.value)
	
	# right subtree: update minVal
	rightIsValid = validateBstHelper(tree.right, tree.value, maxVal)
	
	return leftIsValid and rightIsValid

