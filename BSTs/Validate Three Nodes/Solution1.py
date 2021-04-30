'''
Determine if node two is between one and three
Solution 1: We check if node one is ancestor, and node three is descendant
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h) ST
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
		return isDescendant(nodeThree, nodeTwo)
    if isDescendant(nodeTwo, nodeThree):
		return isDescendant(nodeOne, nodeTwo)
	return False

def isDescendant(node, target):
	if node is None:
		return False
	if node is target:
		return True
	return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)