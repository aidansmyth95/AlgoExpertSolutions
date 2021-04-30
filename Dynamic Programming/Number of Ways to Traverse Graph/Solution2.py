'''
Uses dynamic programming istead of recursive calls.
'''

# O(nm) ST
def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
	
	for widthIdx in range(1, width + 1):
		for heightIdx in range(1, height + 1):
			if widthIdx == 1 or heightIdx == 1:
				numberOfWays[heightIdx][widthIdx] = 1
			else:
				waysLeft = numberOfWays[heightIdx][widthIdx - 1]
				waysUp = numberOfWays[heightIdx - 1][widthIdx]
				numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
	
	return numberOfWays[heightIdx][widthIdx]