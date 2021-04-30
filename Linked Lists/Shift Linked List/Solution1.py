'''
Classic linked list question.
Mutating LL in-place
'''

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) T | O(1)
def shiftLinkedList(head, k):
    listLength = 1
	listTail = head
	# get linked-list length and tail
	while listTail.next is not None:
		listTail = listTail.next
		listLength += 1
	
	# modulo for large k
	offset = abs(k) % listLength
	# do nothing if no shift
	if offset == 0:
		return head
	
	# get new tail depending on sign of k
	newTailPosition = listLength - offset if k > 0 else offset
	newTail = head
	
	for i in range(1, newTailPosition):
		newTail = newTail.next
	
	# get a reference to the new head - is just after new tail
	newHead = newTail.next
	# new tail is now made a tail - remove .next
	newTail.next = None
	# original tail is now linked to old head
	listTail.next = head
	
	return newHead