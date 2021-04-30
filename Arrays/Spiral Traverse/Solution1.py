'''
Iterative solution

Traversing perimeter of arrays and their internal sub-arrays.

When we have dimensions we can use variables to denote
starting/ending row/cols.
'''
# N = n x m
# O(N) T | O(N) S
def spiralTraverse(array):
    
	result = []

	# declare start/end variables
	startC = 0
	startR = 0
	endC = len(array[0]) - 1
	endR = len(array) - 1
	while startC <= endC and startR <= endR:
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

		startR += 1
		startC += 1
		endC -= 1
		endR -= 1

	return result
		