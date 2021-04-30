# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space.
# This is an example where iterative has better
# O(N) space than recursive implementation
# We simply don't use additional memory

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target-closest) > abs(target-currentNode.value):
			closest = currentNode.value
		# move tree
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
