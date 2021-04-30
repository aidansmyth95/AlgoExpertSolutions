'''
valid path does not necessarily have to go through root.
Path is valid if no branch/fork in path.
Could be negative numbers in our tree.

Temp = max(LS + V, V)
Temp2 = max(temp + RS, temp)
'''

# O(n) T - MPS for all values
# O(log(n)) - On average. Binary tree, stack has log(n) calls at most.
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	''' Returns MPS as a branch and a running MPS '''
	if tree is None:
		return (0, float("-inf"))
	
	# LSB, LS = mps(L)
	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	# RSB, RS = mps(R)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
	
	# MCSB = max(LSB, RSB) - max child branch (not triangle)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	
	# MSB = max(MCSB + V, V) - max combo with parent
	value = tree.value
	maxSumAsBranch = max(value, maxChildSumAsBranch + value)
	
	# MST = max(MSB, LSB + V + RSB) - a triangle/root or branch
	maxSumAsRootNode = max(value + leftMaxSumAsBranch + rightMaxSumAsBranch, maxSumAsBranch)
	
	# RMPS = max(LS, RS, MST)
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
	
	# return (MSB, MPS)
	return (maxSumAsBranch, maxPathSum)