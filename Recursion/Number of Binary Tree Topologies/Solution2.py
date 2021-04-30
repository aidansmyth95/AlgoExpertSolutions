# O(n^2) T | O(n) S
def numberOfBinaryTreeTopologies(n):
    cache = [1]
	for m in range(1, n + 1):
		numTrees = 0
		for leftTreeSize in range(m):
			rightTreeSize = m - 1 - leftTreeSize
			numLeftTrees = cache[leftTreeSize]
			numRightTrees = cache[rightTreeSize]
			numTrees += numLeftTrees * numRightTrees
		cache.append(numTrees)
	return cache[n]