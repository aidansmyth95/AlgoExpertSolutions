'''
Last digit is MSB
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n,m)) ST
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedList = LinkedList(0)
	currentNode = newLinkedList
	carry = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	
	while nodeOne is not None or nodeTwo is not None or carry != 0:
		# get two values to add
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		sumOfValues = valueOne + valueTwo + carry
		
		newValue = sumOfValues % 10
		newNode = LinkedList(newValue)
		currentNode.next = newNode
		currentNode = newNode
		
		carry = sumOfValues // 10
		
		# move nodes
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
	
    return newLinkedList.next
