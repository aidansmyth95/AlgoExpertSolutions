'''
Recursive solution

Traversing perimeter of arrays and their internal sub-arrays.

When we have dimensions we can use variables to denote
starting/ending row/cols.
'''
# N = n x m
# O(N) T | O(N) S (only 1 recursive call on stack per perimitter, so small)
def spiralTraverse(array):
    
	result = []
	startC = 0
	startR = 0
	endC = len(array[0]) - 1
	endR = len(array) - 1
	# recursive function
	spiralFill(array, startR, endR, startC, endC, result)
	return result


def spiralFill(array, startR, endR, startC, endC, result):

	# return when we reach this condition
	if startC > endC or startR > endR:
		return

	# -> inclusive
	for col in range(startC, endC + 1):
		result.append(array[startR][col])

	# down
	for row in range(startR + 1, endR + 1):
		result.append(array[row][endC])

	# <-
	for col in reversed(range(startC, endC)):
		# we don't want to repeat if startRow == endRow
		if startR == endR:
			break
		result.append(array[endR][col])


	# up
	for row in reversed(range(startR + 1, endR)):
		# we don't want to repeat if startC == endC
		if startC == endC:
			break
		result.append(array[row][startC])

	spiralFill(array, startR+1, endR-1, startC+1, endC-1, result)
		