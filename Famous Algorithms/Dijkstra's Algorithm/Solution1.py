'''
Extremely famous algo.
Shorted dtist between node and vertices.

Graph in this problem is directed positive edges.
Weight of edge is the length of edge. We only have positive weights here.
No self loops are present in this problem.
-1 means we cannot reach vertex.

We build adjacency list. If we have to look at every possible path, that can
be very efficient. Dijkstras keeps track of what it has already seen to avoid
this inefficiency. Table stores current shorted path to nodes.

0	1	2	3	4	5
----------------------
0	Inf	-	-	-	-		- = Inf
0	7	Inf	-	-	-		maintain a visited set {}
0	7	13	27	10	-
0	7	13	27	10	-
We can skip edge 3->4, since node 4 had a shorted distance to it than to get to
node 3, so we can skip it.
Once set it filled, we stop.

Solution 1 is the inefficient way to find min distance - a for loop O(V)
Solution 2 will be better time complexity - we use a min heap
'''

# O(v^2 + e) T | O(V) S
def dijkstrasAlgorithm(start, edges):
    
	numberOfVertices = len(edges)
	
	# set all to inf except index start which is 0
	minDistances = [float("inf") for _ in range(numberOfVertices)]
	minDistances[start] = 0
	
	visited = set()
	
	while len(visited) < numberOfVertices:
		vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
		
		if currentMinDistance == float("inf"):
			break
			
		visited.add(vertex)
		
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
			
			if destination in visited:
				continue

			# update if a new min distance
			newPathDistance = currentMinDistance + distanceToDestination
			if newPathDistance < minDistances[destination]:
				minDistances[destination] = newPathDistance
	
	return list(map(lambda x: -1 if x == float("inf") else x, minDistances))

def getVertexWithMinDistance(distances, visited):
	currentMinDistance = float("inf")
	vertex = -1
	
	for vertexIdx, distance in enumerate(distances):
		if vertexIdx in visited:
			continue
		if distance < currentMinDistance:
			vertex = vertexIdx
			currentMinDistance = distance
	
	return vertex, currentMinDistance
