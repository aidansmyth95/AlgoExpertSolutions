'''
Graph is a grid in this case, and we can only move right and down.
Solution 1: We can do better than this.
'''

# O(2^(n+m)) T | O(n+m) S -> we can do better
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
		return 1
	
	return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
