'''
SOrted is ascending order.
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) T | O(1) S
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next
		
		currentNode.next = nextDistinctNode
		# we change our current node and do for next node in while loop...
		currentNode = nextDistinctNode
	return linkedList
