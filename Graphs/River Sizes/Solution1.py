'''
This can be treated as a graph traversal problem.
Each node has neighbours.
At every node, if 1, depth first or breadth first search all 1s in its river.
Keep track of nodes that we have already explored in a matrix.
'''

# O(WH) ST
def riverSizes(matrix):
	sizeResults = []
    visited = [[False for x in row] for row in matrix]
	# start traversing
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			if visited[r][c]:
				# skip it
				continue
			traverseNode(matrix, r, c, visited, sizeResults)
	return sizeResults

def traverseNode(matrix, r, c, visited, sizeResults):
	currentRiverSize = 0
	nodesToExplore = [[r, c]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		r = currentNode[0]
		c = currentNode[1]
		if visited[r][c]:
			continue
		visited[r][c] = True
		if matrix[r][c] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbours = getUnvisitedNeighbours(r, c, matrix, visited)
		for neighbour in unvisitedNeighbours:
			nodesToExplore.append(neighbour)
	if currentRiverSize > 0:
		sizeResults.append(currentRiverSize)
		
		
def getUnvisitedNeighbours(r, c, matrix, visited):
	unvisitedNeighbours = []
	# check above
	if r > 0 and not visited[r-1][c]:
		unvisitedNeighbours.append([r-1, c])
	# check below
	if r < len(matrix) - 1 and not visited[r+1][c]:
		unvisitedNeighbours.append([r+1, c])
	# check to right
	if c > 0 and not visited[r][c-1]:
		unvisitedNeighbours.append([r, c-1])	
	# check to left
	if c < len(matrix[0]) - 1 and not visited[r][c+1]:
		unvisitedNeighbours.append([r, c+1])
	return unvisitedNeighbours