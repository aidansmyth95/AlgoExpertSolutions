'''
Solution 2: Iterative implementation of solution 1.
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(h) T | O(1) S
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
		return isDescendant(nodeThree, nodeTwo)
    if isDescendant(nodeTwo, nodeThree):
		return isDescendant(nodeOne, nodeTwo)
	return False

def isDescendant(node, target):
	while node is not None and node is not target:
		node = node.left if target.value < node.value else node.right
	
	return node is target
