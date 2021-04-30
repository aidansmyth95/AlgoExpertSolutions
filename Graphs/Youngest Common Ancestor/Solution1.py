'''
Tree problem. Direction is only going upwards (ancestor).

Get two descendants to same level.
Then find youngest common ancestor.

Get depth by iterating up to top.
'''

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) T | O(1) S
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthD1 = getDepth(descendantOne, topAncestor)
	depthD2 = getDepth(descendantTwo, topAncestor)
	if depthD1 > depthD2:
		return backTrackAncestralTree(
			descendantOne, descendantTwo, depthD1 - depthD2)
	else:
		return backTrackAncestralTree(
			descendantTwo, descendantOne, depthD2 - depthD1)	

def getDepth(node, topAncestor):
	depth = 0
	nodeTmp = node
	while nodeTmp != topAncestor:
		nodeTmp = nodeTmp.ancestor
		depth += 1
	return depth

def backTrackAncestralTree(deepestNode, shallowestNode, diff):
	# remove difference
	while diff > 0:
		deepestNode = deepestNode.ancestor
		diff -= 1
	# keep moving up until they equal
	while deepestNode != shallowestNode:
		deepestNode = deepestNode.ancestor
		shallowestNode = shallowestNode.ancestor
	return deepestNode