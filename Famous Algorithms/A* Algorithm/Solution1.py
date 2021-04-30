'''
Shortest manhatten distance between two points, avoiding obstacles.
We return an array of idx of the path traversed from start node to end node
If no path, return []

Informed search algorithm, where we use a heuristic (educated guess).
Goal is to visit as few nodes as possible.

We decide what node to visit based on 3 scores:
H - heuristic score value
G - Current shortest Manhatten distance to current node
F = G + H
We look for nodes with smallest F score.
Start node has a G score of 0.

Only update node if G score will be less than it currently is.
'''

class Node:
	def __init__(self, row, col, value):
		self.id = str(row) + "-" + str(col)
		self.row = row
		self.col = col
		self.value = value
		self.distanceFromStart = float("inf")
		self.estimatedDistanceToEnd = float("inf")
		self.cameFrom = None

# O (WH log(WH)) T | O(WH) S
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
	startNode = nodes[startRow][startCol]
	endNode = nodes[endRow][endCol]
	startNode.distanceFromStart = 0
	startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)
	
	# create MinHeap of nodes starting at startNode
	nodesToVisit = MinHeap([startNode])
	
	while not nodesToVisit.isEmpty():
		currentMinDistanceNode = nodesToVisit.remove()
		
		if currentMinDistanceNode == endNode:
			break
			
		neighbours = getNeighbourNodes(currentMinDistanceNode, nodes)
		for n in neighbours:
			if n.value == 1:
				continue
			
			tentativeDistanceToNeighbour = currentMinDistanceNode.distanceFromStart + 1
			
			if tentativeDistanceToNeighbour >= n.distanceFromStart:
				continue
			
			n.cameFrom = currentMinDistanceNode
			n.distanceFromStart = tentativeDistanceToNeighbour
			n.estimatedDistanceToEnd = tentativeDistanceToNeighbour + \
				calculateManhattanDistance(n, endNode)
			
			if not nodesToVisit.containsNode(n):
				nodesToVisit.insert(n)
			else:
				nodesToVisit.update(n)
				
	return reconstructPath(endNode)
	
	
	
def initializeNodes(graph):
	nodes = []
	for i, row in enumerate(graph):
		nodes.append([])
		for j, value in enumerate(row):
			nodes[i].append(Node(i, j, value))
	return nodes

def calculateManhattanDistance(currentNode, endNode):
	currentRow = currentNode.row
	currentCol = currentNode.col
	endRow = endNode.row
	endCol = endNode.col
	
	return abs(currentRow - endRow) + abs(currentCol - endCol)


def getNeighbourNodes(node, nodes):
	neighbours = []
	numRows = len(nodes)
	numCols = len(nodes[0])
	row = node.row
	col = node.col
	if row < numRows - 1:
		neighbours.append(nodes[row+1][col])
	if row > 0:
		neighbours.append(nodes[row-1][col])
	if col < numCols - 1:
		neighbours.append(nodes[row][col+1])
	if col > 0:
		neighbours.append(nodes[row][col-1])
	return neighbours
		
def reconstructPath(endNode):
	if not endNode.cameFrom:
		return []
	currentNode = endNode
	path = []
	
	while currentNode is not None:
		path.append([currentNode.row, currentNode.col])
		currentNode = currentNode.cameFrom
	return path[::-1] # reverse path order so start to end


class MinHeap:
	def __init__(self, array):
		self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array) }
		self.heap = self.buildHeap(array)
		
	def isEmpty(self):
		return len(self.heap) == 0
	
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if (
				childTwoIdx != -1 and \
			   	heap[childTwoIdx].estimatedDistanceToEnd < \
					heap[childOneIdx].estimatedDistanceToEnd
			   ):
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
	
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

	def remove(self):
		if self.isEmpty():
			return
		
		self.swap(0, len(self.heap) - 1, self.heap)
		node = self.heap.pop()
		del self.nodePositionsInHeap[node.id]
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return node

	def insert(self, node):
		self.heap.append(node)
		self.nodePositionsInHeap[node.id] = len(self.heap) - 1
		self.siftUp(len(self.heap) - 1, self.heap)
		
	def swap(self, i, j, heap):
		self.nodePositionsInHeap[heap[i].id] = j
		self.nodePositionsInHeap[heap[j].id] = i
		heap[i], heap[j] = heap[j], heap[i]
	
	def containsNode(self, node):
		return node.id in self.nodePositionsInHeap
	
	def update(self, node):
		self.siftUp(self.nodePositionsInHeap[node.id], self.heap)