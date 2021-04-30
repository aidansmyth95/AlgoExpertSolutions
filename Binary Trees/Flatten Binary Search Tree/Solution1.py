# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) ST - we could improve space complexity though...
def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root, [])
	for i in range(len(inOrderNodes) - 1):
		leftNode = inOrderNodes[i]
		rightNode = inOrderNodes[i+1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return inOrderNodes[0]

def getNodesInOrder(tree, array):
	if tree is not None:
		getNodesInOrer(tree.left, array)
		array.append(tree)
		getNodesInOrer(tree.right, array)
	return array