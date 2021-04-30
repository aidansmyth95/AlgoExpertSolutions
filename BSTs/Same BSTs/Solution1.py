'''
Left of tree: less than node
Right of tree: Greater than or equal to node
Idea to solve: recursively compare first two values & length. If all ok, split
subtrees into left and right and continue checks for next layer
'''

# O(n^2) ST - Iterate through all N elements for each of N elements.
# We are creating all these extra calls, O(n^2). O(d) on the call stack.
# We can do better by not using these additional arrays.
def sameBsts(arrayOne, arrayTwo):
    # check that length is same
	if len(arrayOne) != len(arrayTwo):
		return False
	
	# if there is nothing left, return True
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	# check that root is the same
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	# check that elements greater than or less than root are of same count
	leftOne, rightOne = getSubtrees(arrayOne)
	leftTwo, rightTwo = getSubtrees(arrayTwo)

	# recursive call
	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSubtrees(array):
	root = array[0]
	left = []
	right = []
	for i in range(1, len(array)):
		if array[i] < root:
			left.append(array[i])
		else:
			right.append(array[i])
	return left, right

def sameNodes(arrayOne, arrayTwo):
	stack = {}
	for item in arrayOne:
		stack[item] = True
	print(stack)
	for item in arrayTwo:
		if not stack[item]:
			return False
	return True