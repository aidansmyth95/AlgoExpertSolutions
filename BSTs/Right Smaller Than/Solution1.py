'''
Number of elements to right of array index that are smaller than it.
Solution 1: Nested for loop.
To get a better but realistic optimal solution, we would have O(nlogn) T.
We don't want to sort the array.
So how about a binary search tree data structure?
Solution 2: BST. Insert from right to left into tree. Insertion takes log(n),
so if we have n insertions, we have nlogn time.
We need to keep track of number of smaller nodes, at point of insertion. We
look at left-subtree, how many nodes are there at insert time? That is the
answer. Keep track of left subtree size at every node.
'''

# O(n^2) T | O(n) S
def rightSmallerThan(array):
    rightSmallerCounts = []
	for i in range(len(array)):
		rightSmallerCount = 0
		for j in range(i + 1, len(array)):
			if array[j] < array[i]:
				rightSmallerCount += 1
		rightSmallerCounts.append(rightSmallerCount)
	return rightSmallerCounts