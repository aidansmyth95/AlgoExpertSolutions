# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) T | O(1) S
def nodeSwap(head):
    tempNode = LinkedList(0)
	tempNode.next = head
	
	prevNode = tempNode
	while prevNode.next is not None and prevNode.next.next is not None:
		firstNode = prevNode.next
		secondNode = prevNode.next.next
		
		firstNode.next = secondNode.next
		secondNode.next = firstNode
		prevNode.next = secondNode

		prevNode = firstNode
		
	return tempNode.next