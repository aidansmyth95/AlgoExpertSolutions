'''
Finding a loop in a singly linked list.

Traverse entire linked list, add nodes to hash table approach:
	- works, but is sub-optimal
	- requires hash table
	
Solution:
	- traverse list with two pointers.
	- Second pointer skips a node every step.
	- when the two pointers overlap, there is a cycle proven.

First travels x distance, second travels 2x.
Distance between starting node and loop origin is d
Distancebetween loop origin and overlap is distance d + p
Remainder distance is r

T is total distance of linked list.
d + p + r = full list distance. When we overlap we are r away from loop origin

F = x = d + p
S = 2x = 2d + 2p
T = 2D + 2P - P = 2D + P
R = T - P - D
R = 2D + P - P - D = D	-> R = D

What does this mean? It means that if we move first pointer back to start,
and move second and first pointers at same pace, they will converge on loop
origin (distance D away from both, since R = D).
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) T | O(1) S
def findLoop(head):
    first = head.next
	second = head.next.next
	while first != second:
		first = first.next
		second = second.next.next
	# at this stage they have overlapped. Reset first pointer,
	# and move both from here out at same pace
	first = head
	while first != second:
		first = first.next
		second = second.next
	return first
	
