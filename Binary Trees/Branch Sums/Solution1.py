# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isLeaf(node):
	return node.right == None and node.left == None

# O(n) time | O(n) space - we need to visit all the branches
# this time, cannot do log(N)
# Space is recursive calls so O(log(N)), but the branch sums
# (or number of leaf nodes) you will have approx N/2 branches
# to sum, so O(N) space complexity dominates.

def branchSums(root):
    sums = []
	calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, running_sum, sums):
	# if None, return
	if node is None:
		return

	# update running sum
	running_sum += node.value
	# if leaf, append running sum to sums list and 
	if isLeaf(node):
		sums.append(running_sum)
	else:
		# keep moving leftand right  recursively
		calculateBranchSums(node.left, running_sum, sums)
		calculateBranchSums(node.right, running_sum, sums)
