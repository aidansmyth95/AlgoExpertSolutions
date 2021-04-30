# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) T | O(1) S
def removeKthNodeFromEnd(head, k):
    counter = 1
	first = head
	second = head
	while counter <= k:
		# iterate k nodes to set second pointer k ahead of first
		second = second.next
		counter += 1
	# if second is None, we are moving head
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		# then move both pointers at once, until second reaches end
		second = second.next
		first = first.next
	first.next = first.next.next
