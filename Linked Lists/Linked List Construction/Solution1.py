'''
Doubly-linked: pointers to prev and next.
Head and tail point to None for out of bounds.
Let us put Head on left, and tail on right.
next is ->
prev is <-
'''

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

	# O(1) ST
    def setHead(self, node):
        if self.head is None:
			# if single node linked list, node is head and tail
			self.head = node
			self.tail = node
		else:
			# else we just insert before the head, making it the new head
			self.insertBefore(self.head, node)

	# O(1) ST
    def setTail(self, node):
        if self.tail is None:
			# if single node linked list, node is head and tail
			self.setHead(node)
		else:
			# else we just insert after the tail, making it the new tail
			self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
		# if we are dealing with a linked list with only one node,
		# and that node is what we are trying to insert, no-op
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		# next, account for node already being in linked list
		# remove the node from linked list
		self.remove(nodeToInsert)
		# then start with the actual insertion - updating the pointers
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		# if node was a head, nodeToInsert must become head
		if node.prev is None:
			self.head = nodeToInsert
		else:
			# update previous nodes next pointer to point to inserted node
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
		# same idea as insertBefore
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		# check if next node is None (node was tail)
		if node.next is None:
			self.tail = nodeToInsert
		else:
			# update tail to point prev to inserted node
			node.next.prev = nodeToInsert
		# update node to point to inserted node
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # is the position 1?
		if position == 1:
			# setHead
			self.setHead(nodeToInsert)
			return
		# Move a pointer through linked list until pointing at node or end
		currentNode = self.head
		currentPosition = 1
		while currentNode is not None and currentPosition != position:
			currentNode = currentNode.next
			currentPosition += 1
		# If at end, insert at tail.
		if currentNode is not None:
			# if not end, insertBefore.
			self.insertBefore(currentNode, nodeToInsert)
		else:
			# set as tail
			self.setTail(nodeToInsert)

	# O(N) T | O(1) S
    def removeNodesWithValue(self, value):
        # iterate through list until value found, and remove
		currentNode = self.head
		while currentNode is not None:
			nodeToRemove = currentNode
			currentNode = currentNode.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

	# O(1) ST
    def remove(self, node):
        # if node to remove is head, point head somewhere else
		if node == self.head:
			self.head = self.head.next
		# if node to remove is tail, point tail somewhere else
		if node == self.tail:
			self.tail = self.tail.prev
		# update node's neighbors' pointers
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		# remove node's pointers
		node.next = None
		node.prev = None
			
	# O(N) T | O(1) S
    def containsNodeWithValue(self, value):
        node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
