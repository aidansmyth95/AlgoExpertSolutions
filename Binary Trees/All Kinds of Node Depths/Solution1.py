'''
This is very simple method with good complexity. No brainer
'''

# O(n) T | O(h) S
def allKindsOfNodeDepths(root, depthSum=0, depth=0):
    if root is None:
		return 0
	
	depthSum += depth
	return(
		depthSum + \
		allKindsOfNodeDepths(root.left, depthSum, depth + 1) + \
		allKindsOfNodeDepths(root.right, depthSum, depth + 1)
	)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
