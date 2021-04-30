'''
Cycle - connected vertices in a closed chain. First and last are same.
Number of V is length of E
Directed graph.
All edges are same length
Adjacency list of outbound edges.
Multiple ways to solve this problem.
Good practice: to draw graph as a tree and look for interesting things ....
......
... If there is an edge from descendant to ancestor, we have a cycle!!!
'''

# O(V+E) T | O(V) S
def cycleInGraph(edges):
	visited = [False for _ in range(len(edges))]
	inStack = [False for _ in range(len(edges))]
	numberOfNodes = len(edges)
	
	for node in range(numberOfNodes):
		if not visited[node]:
			containsCycle = isNodeInCycle(node, edges, visited, inStack)
			if containsCycle:
				return True
	return False

def isNodeInCycle(node, edges, visited, inStack):
	# update visited
	visited[node] = True
	# update inStack
	inStack[node] = True

	# get outgoing edges
	outNodes = edges[node]
	for outNode in outNodes:
		if not visited[outNode]:
			# if not already visited, ercusive call on that node
			containsCycle = isNodeInCycle(outNode, edges, visited, inStack)
			if containsCycle:
				return True
		elif inStack[outNode]:
			# if node is already inStack, we have a cycle
			return True
	
	# remove original node from inStack at end
	inStack[node] = False
	return False