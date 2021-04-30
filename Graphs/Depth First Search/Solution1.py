# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# Note: This is a Graph problem, not BST!
	# O(V+E) time | O(V) space
	# Space complexity:
	# - array of V differnt nodes
	# - worst case scenario would be O(V) frames to call stack
    def depthFirstSearch(self, array):
        # recursive-like (not recursive)
		# add node to final array
		# for every child call function and pass in final array
		
		# append current node's name to array
		array.append(self.name)
		for child in self.children:
			# this will keep going until no more children (leaf node)
			child.depthFirstSearch(array)
			# then the next child is searched
		return array
