'''
Quite difficult to remember or implement.
Second solution allows for smaller space. We just do recursion.
We use pointers to keep track of where in tree we are.
'''

# O(n^2) T | O(d) S
def sameBsts(arrayOne, arrayTwo):
   	return sameBstsHelper(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def sameBstsHelper(arrayOne, arrayTwo, rootOneIdx, rootTwoIdx, minVal, maxVal):
	''' Roots of current subtrees we are parsing, and their min/max vals ... '''
	if rootOneIdx == -1 or rootTwoIdx == -1:
		return rootOneIdx == rootTwoIdx
	
	if arrayOne[rootOneIdx] != arrayTwo[rootTwoIdx]:
		return False
	
	leftRootOneIdx = getLeftSubtreeIdx(arrayOne, rootOneIdx, minVal)
	leftRootTwoIdx = getLeftSubtreeIdx(arrayTwo, rootTwoIdx, minVal)
	rightRootOneIdx = getRightSubtreeIdx(arrayOne, rootOneIdx, maxVal)
	rightRootTwoIdx = getRightSubtreeIdx(arrayTwo, rootTwoIdx, maxVal)
	
	currentValue = arrayOne[rootOneIdx]
	# max value is right above
	leftAreSame = sameBstsHelper(arrayOne, arrayTwo, leftRootOneIdx, leftRootTwoIdx, minVal, currentValue)
	# min value is right above
	rightAreSame = sameBstsHelper(arrayOne, arrayTwo, rightRootOneIdx, rightRootTwoIdx, currentValue, maxVal)
	
	return leftAreSame and rightAreSame
	
def getLeftSubtreeIdx(array, startingIdx, minVal):
	''' Find idx of first smaller value after startingIdx. Must be >= minVal,
		which is the previous parent node's value. If not, then value must be
		to left of a previous ancestor.
	'''
	for i in range(startingIdx + 1, len(array)):
		if array[i] < array[startingIdx] and array[i] >= minVal:
			return i
	return -1
	
def getRightSubtreeIdx(array, startingIdx, minVal):
	''' Find idx of first smaller value after startingIdx. Must be >= minVal,
		which is the previous parent node's value. If not, then value must be
		to left of a previous ancestor.
	'''
	for i in range(startingIdx + 1, len(array)):
		if array[i] >= array[startingIdx] and array[i] < minVal:
			return i
	return -1