'''
We need three pointers: previous, current and next nodes
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) T | O(1) S
def reverseLinkedList(head):
    previousNode, currentNode = None, head
	while currentNode is not None:
		# get next pointer first
		nextNode = currentNode.next
		# then point current pointer to previous node
		currentNode.next = previousNode
		# then move pointers to their successors and repeat
		previousNode = currentNode
		currentNode = nextNode
	return previousNode
