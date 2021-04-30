'''
In Graph we have Vertices and Edges.
Complexity of this algorithm is involved.
Time = O(V+E), because for each V we do E node adds.
'''

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

	# we do not use this
    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(V+E) T | O(V) S
    def breadthFirstSearch(self, array):
		# add all children to queue
		# get first in item from queue and append to list
		# then do the same for each childs children (left to right)
		queue = [self]
		while len(queue) > 0:
			# get first in
			current = queue.pop(0)
			array.append(current.name)
			for child in current.children:
				queue.append(child)
		return array
