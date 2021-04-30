# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
		return linkedList
	
	firstHalfHead = linkedList
	secondHalfHead = splitLinkedList(linkedList)
	
	reverseSecondHalfHead = reverseLinkedList(secondHalfHead)
	
	return interweaveLinkedLists(firstHalfHead, reverseSecondHalfHead)

def splitLinkedList(linkedList):
	slowIterator = linkedList
	fastIterator = linkedList
	while fastIterator is not None and fastIterator.next is not None:
		slowIterator = slowIterator.next
		fastIterator = fastIterator.next.next
	
	secondHalfHead = slowIterator.next
	slowIterator.next = None
	return secondHalfHead

def interweaveLinkedLists(linkedList1, linkedList2):
	linkedList1Iterator = linkedList1
	linkedList2Iterator = linkedList2
	while linkedList1Iterator is not None and linkedList2Iterator is not None:
		linkedList1IteratorNext = linkedList1Iterator.next
		linkedList2IteratorNext = linkedList2Iterator.next
		
		linkedList1Iterator.next = linkedList2Iterator
		linkedList2Iterator.next = linkedList1IteratorNext
		
		linkedList1Iterator = linkedList1IteratorNext
		linkedList2Iterator = linkedList2IteratorNext
		
	return linkedList1

def reverseLinkedList(linkedList):
	prevNode, currNode = None, linkedList
	while currNode is not None:
		nextNode = currNode.next
		currNode.next = prevNode
		prevNode = currNode
		currNode = nextNode
	return prevNode
		
		
