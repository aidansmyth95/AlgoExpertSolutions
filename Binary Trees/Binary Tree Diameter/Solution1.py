'''
Diamater is length of the longest path (edges not nodes).

Tactic:
Recursive method
Return diameter and height
Navigate to leaf nodes.
Then moving up:
- increment height
- update diameter: max(left sub, right sub, path through root)
'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(N) T | O(d) S
def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	
	# leaves there is no height or diameter
	if tree is None:
		return TreeInfo(0,0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	# get longest path through root by adding subtree diameters
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	
	# max diameter is max of subtree diameters and longest path
	oldMaxDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	newMaxDiameter = max(longestPathThroughRoot, oldMaxDiameter)
	
	# increment height
	currHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	return TreeInfo(newMaxDiameter, currHeight)
	
class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height
