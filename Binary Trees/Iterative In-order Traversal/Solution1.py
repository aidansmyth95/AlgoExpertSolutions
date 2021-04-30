'''
Every node keeps track of parent nodes
Iterative in order traversal - left-most to right-most

You can call callback or not, based on previous node you traversed.
We see this scenario at root for example. We don not want to re-explore all
left subtree again.
If previous node is parent, we must go left & down
'''

# O(n) T | O(1) S
def iterativeInOrderTraversal(tree, callback):
    previousNode = None
	currentNode = tree
	
	while currentNode is not None:
		# if previous node is parent
		if previousNode is None or previousNode == currentNode.parent:
			if currentNode.left is not None:
				nextNode = currentNode.left
			else:
				# if no left node, call callback
				callback(currentNode)
				nextNode = currentNode.right if currentNode.right is not None \
					else currentNode.parent
		elif previousNode == currentNode.left:
			callback(currentNode)
			nextNode = currentNode.right if currentNode.right is not None else \
				currentNode.parent
		else:
			# we are going up to parent
			nextNode = currentNode.parent
		previousNode = currentNode
		currentNode = nextNode
		
	
