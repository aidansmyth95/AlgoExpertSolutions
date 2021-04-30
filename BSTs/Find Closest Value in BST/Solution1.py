# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space.

# Most BST methods are O(log(n)) since we are removing half of
# tree most of time when we go left or right.
# Space: If recursive, we call multiple times and use up frames on call stack
# and extra memory.

def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target-closest) > abs(target-tree.value):
		# update closest if distance is smaller than current
		closest=tree.value
	# move tree by running recursively
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
