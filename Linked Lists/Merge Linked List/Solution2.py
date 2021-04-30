'''
Recursive solution, worse space complexity than iterative one.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n+m) T | O(n+m) S
def mergeLinkedLists(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
	return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1, p2, p1Prev):
	if p1 is None:
		p1Prev.next = p2
		return
	if p2 is None:
		return
	
	if p1.value < p2.value:
		# easiest case - no mutation keep moving forwards in LL1
		recursiveMerge(p1.next, p2, p1)
	else:
		if p1Prev is not None:
			# starts out as None, so can't call next
			# p1Prev point to p2 now
			p1Prev.next = p2
		newP2 = p2.next
		p2.next = p1
		recursiveMerge(p1, newP2, p2)
