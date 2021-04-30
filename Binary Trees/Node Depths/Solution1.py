# O(n) time and O(h) space, where n are ndes and h is height of BST

def nodeDepths(root, depth=0):
	# If root is leaf, we have no depth
	if root is None:
		return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
