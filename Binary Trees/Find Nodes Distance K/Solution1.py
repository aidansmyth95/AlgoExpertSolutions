# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

'''
Target is an integer than specifies binary tree node value.
All values in tree are unique.
Distance is number of edges between two nodes, up and down.
We need to:
	1. Determine parent nodes - create and use a mapping from node to parent.
		Use dfs to do this.
	2. Locate target node - use our created data struct map to find parent,
		and then find the correct child
	3. BFS to locate nodes that are k away from target.
		Create a queue with node, distance. Add neighbours to queue.
		Neighbours are left, right, parent.
		If we find a node we have already considered, so not add to queue.
		This data struct will be a set of seen nodes.
		Stop once distance is == k and all nodes in queue have this distance.
		We have used BFS for this reason, we are expanding out and distance is
		consistent from target. Then pop all from queue and return all of them.

'''

# O(n) ST - number of edges will never be > n. We use n space for struct
def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
	populateNodesToParents(tree, nodesToParents)
	targetNode = getNodeFromValue(target, tree, nodesToParents)
    return bfsForDistanceK(targetNode, nodesToParents, k)

def bfsForDistanceK(targetNode, nodesToParents, k):
	# we are going to be popping from start of queue, which in Python takes
	# O(n) time. If we had packages, we could use a deq or double ended queue..
	queue = [(targetNode, 0)] # start at distance 0
	seen = {targetNode.value}
	while len(queue) > 0:
		currentNode, distanceFromTarget = queue.pop(0)
		# if we get to stage where k away, all values in queue are also
		# k away. Add them to the returned list
		if distanceFromTarget == k:
			nodesDistanceK = [node.value for node, _ in queue]
			nodesDistanceK.append(currentNode.value)
			return nodesDistanceK
		# look up neighbours
		connectedNodes = [
			currentNode.left, currentNode.right,
			nodesToParents[currentNode.value]]
		for node in connectedNodes:
			# if for when not to add node
			if node is None or node.value in seen:
				continue
			seen.add(node.value)
			queue.append((node, distanceFromTarget+1))
	return []
	
def getNodeFromValue(value, tree, nodesToParents):
	# if root node is target
	if tree.value == value:
		return tree
	# use populated struct to get parent
	nodeParent = nodesToParents[value]
	# check children and return correct child
	if nodeParent.left and nodeParent.left.value == value:
		return nodeParent.left

	return nodeParent.right

def populateNodesToParents(node, nodesToParents, parent=None):
	if node:
		# add value as key and parent node objct as value
		nodesToParents[node.value] = parent
		# do for children
		populateNodesToParents(node.left, nodesToParents, parent=node)
		populateNodesToParents(node.right, nodesToParents, parent=node)