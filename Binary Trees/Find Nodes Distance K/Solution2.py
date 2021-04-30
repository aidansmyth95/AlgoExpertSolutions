# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


'''
Rather from starting and going out from targert node in BFS, start at
root node and DFS towards the target node. Allows us to avoid finding parents
of all our nodes, and having to find the target node.

1. Depth first search in both subtree, return -1 for subtree not containing target.
2. When target is found
	- return L for subtree with target
	- go k down from target and add to list
	- go K - L down on other subtree and add those to list too
'''

# O(n) ST
def findNodesDistanceK(tree, target, k):
    nodesDistanceK = []
	findDistanceFomNodeToTarget(tree, target, k, nodesDistanceK)
	return nodesDistanceK

def findDistanceFomNodeToTarget(node, target, k, nodesDistanceK):
	
	if node is None:
		return -1
	
	if node.value == target:
		# DFS for subtree nodes from target
		addSubtreeNodesAtDistanceK(node, 0, k, nodesDistanceK)
		# indicate we have found target
		return 1
	
	# is node in left or right subtree: -1 tells us answer
	leftDistance = findDistanceFomNodeToTarget(node.left, target, k, nodesDistanceK)
	rightDistance = findDistanceFomNodeToTarget(node.right, target, k, nodesDistanceK)
	
	if leftDistance == k or rightDistance == k:
		# then this node is k away from target node
		nodesDistanceK.append(node.value)
		
	# if target is in left subtree, we need to look for nodes in right subtree
	# that are k away from it
	if leftDistance != -1:
		addSubtreeNodesAtDistanceK(node.right, leftDistance + 1, k, nodesDistanceK)
		return leftDistance + 1
	if rightDistance != -1:
		addSubtreeNodesAtDistanceK(node.left, rightDistance + 1, k, nodesDistanceK)
		return rightDistance + 1
	
	return -1


def addSubtreeNodesAtDistanceK(node, distance, k, nodesDistanceK):
	if node is None:
		return
	if distance == k:
		nodesDistanceK.append(node.value)
	else:
		# recursive simulation of DFS
		addSubtreeNodesAtDistanceK(node.left, distance+1, k, nodesDistanceK)
		addSubtreeNodesAtDistanceK(node.right, distance+1, k, nodesDistanceK)
	
	