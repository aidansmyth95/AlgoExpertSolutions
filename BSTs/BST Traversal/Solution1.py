"""
In-order:
- Sorted array.
1. inOrder(left)
2. append(current)
3. inOrder(right)

Pre-order:
- Like a depth-first search
1. append(current)
2. inOrder(left)
3. inOrder(right)

Post-order:
1. inOrder(left)
2. inOrder(right)
3. append(current)

"""

# O(N) ST for all these Traversals
def inOrderTraverse(tree, array):
	if tree is not None:
		# 1. inOrder(left)
		inOrderTraverse(tree.left, array)
		#2. append(current)
		array.append(tree.value)
		#3. inOrder(right)
		inOrderTraverse(tree.right, array)
	return array


# O(N) ST for all these Traversals
def preOrderTraverse(tree, array):
    if tree is not None:
		# 1. append(current)
		array.append(tree.value)
		# 2. inOrder(left)
		preOrderTraverse(tree.left, array)
		# 3. inOrder(right)
		preOrderTraverse(tree.right, array)
	return array

# O(N) ST for all these Traversals
def postOrderTraverse(tree, array):
    if tree is not None:
		# 1. inOrder(left)
		postOrderTraverse(tree.left, array)
		# 2. inOrder(right)
		postOrderTraverse(tree.right, array)
		# 3. append(current)
		array.append(tree.value)
	return array