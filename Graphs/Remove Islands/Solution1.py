'''
We can treat this as a graph traversal problem BFS or DFS.
Navigate around perimeter. Build up a list of visited nodes.
When this is done, increment row and col and visit all inner matrix idx.
If not in visited list, remove.
'''

# O(WH) ST
def removeIslands(matrix):
    # list of potential island idx - assume all True at start
	borderLand = [[False for col in row] for row in matrix]

	# find all ones that are not islands
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			rowIsBorder = r == 0 or r == len(matrix) - 1
			colIsBorder = c == 0 or c == len(matrix[0]) - 1
			isBorder = rowIsBorder or colIsBorder
			# if border and land, find connected ones
			if isBorder and matrix[r][c] == 1:
				findConnectedLand(matrix, r, c, borderLand)
				
	# then mutate array removing islands accordingly ...
	for r in range(1, len(matrix) - 1):
		for c in range(1, len(matrix[0]) - 1):
			if not borderLand[r][c] and matrix[r][c] == 1:
				matrix[r][c] = 0
	
	return matrix

def findConnectedLand(matrix, r, c, borderLand):
	# here we will want to do a graph search (BFS) to find 
	# connected ones to the matrix[r][c]. Updat borderLand with True.
	connected = [[r, c]]
	
	while len(connected) > 0:
		currentPos = connected.pop(0)
		currentRow, currentCol = currentPos
		# check if already visited
		if borderLand[currentRow][currentCol]:
			continue
		# since this was in stack, we can set it true, and visit its neighbours
		borderLand[currentRow][currentCol] = True
		# check neighbouring nodes and add to stack
		neighbours = getNeighbours(matrix, currentRow, currentCol)
		for neighbour in neighbours:
			newRow, newCol = neighbour
			if matrix[newRow][newCol] == 1:
				connected.append(neighbour)

def getNeighbours(matrix, r, c):
	# create a list of neighbours
	neighbours = []
	
	# up
	if r - 1 >= 0:
		neighbours.append((r - 1, c))
	# down
	if r + 1 < len(matrix):
		neighbours.append((r + 1, c))
	# left
	if c - 1 >= 0:
		neighbours.append((r, c - 1))
	# right
	if c + 1 < len(matrix[0]):
		neighbours.append((r, c + 1))

	return neighbours