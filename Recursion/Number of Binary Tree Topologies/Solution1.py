

# O(VERY BIG) T -> Catalan number
def numberOfBinaryTreeTopologies(n):
    if n == 0:
		return 1
	numTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
		numRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
		numTrees += numLeftTrees * numRightTrees
	return numTrees
