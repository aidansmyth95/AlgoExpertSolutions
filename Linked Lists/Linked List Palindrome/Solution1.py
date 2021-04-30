'''
Singly linked list - is it a palindrome?
Iterative approach or recursive. Lets use iterative here
Half lists using fast and slow pointers. Then reverse one half of linked
list and compare both halves values for equality.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) T | O(1) S
def linkedListPalindrome(head):
    slowNode = head
	fastNode = head
	while fastNode is not None and fastNode.next is not None:
		slowNode = slowNode.next
		fastNode = fastNode.next.next
		
	reversedSecondHalfNode = reverseLinkedList(slowNode)
	firstHalfNode = head

	while reversedSecondHalfNode is not None:
		if reversedSecondHalfNode.value != firstHalfNode.value:
			return False
		reversedSecondHalfNode = reversedSecondHalfNode.next
		firstHalfNode = firstHalfNode.next
	return True

def reverseLinkedList(head):
	previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode