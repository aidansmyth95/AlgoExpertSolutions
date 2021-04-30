'''
Note: node is guaranteed to be in the BT.
Some nodes may have no successor

From what I recall:
- In order recursively is:
	- inOrder(left)
	- visit / append(current)
	- inOrder(right)
	
Easy to implement option: Build a list by appending and check for successor.
We would be O(N) ST though. Works if we do not have parent attribute.

We can do better. We do not need to store or traverse entire tree.

Observation 1: If node has right sub-tree, that its successor is somewhere
there. We would go to leftmost child of subtree and use that as successor.
Successor cannot be in left sub-tree.

Observation 2: If no right sub-tree, it needs to be an ancestor.
We look up until we came from left child of parent.

'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    return findSuccessorHelper(tree, node)

# O(h) T | O(1) S
def findSuccessorHelper(tree, node):
	# Option 1: Left-most node in right sub-tree
	if node.right is not None:
		return getLeftMostChild(node.right)
	# Option 2: Right-most parent
	return getRightMostParent(node)
	

def getLeftMostChild(tree):
	node = tree
	while node.left is not None:
		node = node.left
	return node

def getRightMostParent(tree):
	node = tree
	# while the parent is not none and the parent's right child is the node
	# get new parent
	while node.parent is not None and node.parent.right == node:
		node = node.parent
	return node.parent
