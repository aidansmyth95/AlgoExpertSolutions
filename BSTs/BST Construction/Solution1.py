'''
Insert: straightforward
Remove: Depends on number of children
Searching: Depth-first search (because why not)

BST Property:
- Nodes values must be > nodes to its left, and <= nodes to right

Remove
- If leaf: Just remove it
- If has one child: Child replaces it
- If has two children: Find the smallest (left-most) value in
	the right subtree and replace value with it.
'''


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	# Avg: O(logN) T | O(logN) S
	# Worst: O(N) T | O(N) S
    def insert(self, value):
        if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self
				
	# Big O: Same complexity as insert
    def contains(self, value):
        if value < self.value:
			if self.left is None:
				return False
			else:
				# check for nodes to left
				return self.left.contains(value)
        if value > self.value:
			if self.right is None:
				return False
			else:
				# check for nodes to left
				return self.right.contains(value)
		else:
			return True

    def remove(self, value, parent=None):
		if value < self.value:
			if self.left is not None:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None:
				self.right.remove(value, self)	
		# we have found the value to remove
		else:
			# two children case: find left-most in right sub-tree
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinValue()
				self.right.remove(self.value, self)
			# in case where parent is None: i.e. the root node.
			# you replace with left, or if no left then right
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					# no left or right to replace it with, so pass
					pass
			# a node with only one child or none
			elif parent.left == self:
				parent.left = self.left if self.left is not None else self.right
			# a node with only one child or none
			elif parent.right == self:
				parent.right = self.left if self.left is not None else self.right
		return self


	def getMinValue(self):
		if self.left is None:
			print('f {}'.format(self.value))
			return self.value
		else:
			return self.left.getMinValue()
