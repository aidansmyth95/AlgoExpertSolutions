'''
We are allowed to mutate linked lists.
Need to keep track of several (at least three) pointers at once, non-trivial.
Iterative solution first - better space complexity.

As we iterate through both linked lists, we move pointers.
We need to mutate current node and previous node in linked list.

'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n+m) T | O(1) S
def mergeLinkedLists(headOne, headTwo):
	# three different pointers at any time
	# we are mutating headOne linked-list
    p1 = headOne
	p1Prev = None
	p2 = headTwo
	while p1 is not None and p2 is not None:
		if p1.value < p2.value:
			# easiest case - no mutation keep moving forwards in LL1
			p1Prev = p1
			p1 = p1.next
		else:
			if p1Prev is not None:
				# starts out as None, so can't call next
				# p1Prev point to p2 now
				p1Prev.next = p2
			# then move p1Prev to be p2
			p1Prev = p2
			# then move p2 to be its next value
			p2 = p2.next
			# then point p1Prev back to p1
			p1Prev.next = p1
	# at end of while loop
	if p1 is None:
		# if we ran out of first LL, append LL2 to LL1
		# otherwise we do not do anything, since p1 is setup correctly.
		p1Prev.next = p2
		
	# head to return is smallest head
	return headOne if headOne.value < headTwo.value else headTwo
