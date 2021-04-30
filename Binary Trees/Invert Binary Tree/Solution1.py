'''
Recursive
Keep swapping left and right children reucrsively
'''

def invertBinaryTree(tree):
    # Write your code here.
    return invertBinaryTreeHelper(tree)

# O(N) T | O(d) S
def invertBinaryTreeHelper(tree):
	if tree is None:
		return tree
	
	# swap, even if None
	tree.left, tree.right = tree.right, tree.left
	invertBinaryTreeHelper(tree.left)
	invertBinaryTreeHelper(tree.right)

	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
