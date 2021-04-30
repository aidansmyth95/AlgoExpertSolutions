'''
Dynamic programming.
I like the iterative solutons better, plus they have better time complexity than recursive.
First solution: sub-optimal in time, best in space.
Get all squares, moving top left corner, and then check each to see if square of zeros

'''

# O(n^4) T | O(1) S
def squareOfZeroes(matrix):
    n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				# while in bounds
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol + squareLength - 1
				if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False


# this is time complexity costly! O(len^2) complexity
def isSquareOfZeroes(matrix, r1, c1, r2, c2):
	for row in range(r1, r2 + 1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1, c2 + 1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True