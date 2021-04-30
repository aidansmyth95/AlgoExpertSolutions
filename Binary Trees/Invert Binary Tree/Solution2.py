'''
Iterative
Keep swapping left and right children reucrsively
'''

def invertBinaryTree(tree):
    # Write your code here.
    return invertBinaryTreeHelper(tree)

# O(N) T | O(N) S - due to the queue holding N/2 leaf nodes in a BST
def invertBinaryTreeHelper(tree):
	
	queue = [tree]
	while len(queue) > 0:
		node = queue.pop(0)
		if node is None:
			continue
		node.left, node.right = node.right, node.left
		queue.append(node.left)
		queue.append(node.right)

	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
