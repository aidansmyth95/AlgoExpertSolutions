# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, isBalanced, height):
		self.isBalanced = isBalanced
		self.height = height

# O(n) T | O(h) S
def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
	return treeInfo.isBalanced

def getTreeInfo(node):
	if node is None:
		return TreeInfo(True, -1)
	
	leftInfo = getTreeInfo(node.left)
	rightInfo = getTreeInfo(node.right)
	
	tmp = abs(leftInfo.height - rightInfo.height) <= 1
	isBalanced = leftInfo.isBalanced and rightInfo.isBalanced and tmp
	height = max(leftInfo.height, rightInfo.height) + 1
	
	return TreeInfo(isBalanced, height)
