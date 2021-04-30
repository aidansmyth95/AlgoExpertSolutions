'''
2D array of 9x9, integers 0-9. 0 is an empty space we need to fill.

Every empty cell has 9 possibilities. A lot of possibilities for up to 81
cells. Brute force approach would not be the way to go.

Fill in numbers, check if valid board, stop if invalid board and try another
solution.
'''

# O(1) ST - since we only have 81 cells
def solveSudoku(board):
    solvePartialSudoku(0, 0, board)
	return board

def solvePartialSudoku(row, col, board):
	# helper function that will eventually return completed board
	currentRow = row
	currentCol = col
	
	# valid when we have got to end without backtracking sending us back
	if currentCol == len(board[currentRow]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			# board is completed
			return True
	
	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow, currentCol, board)
	
	return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
	for digit in range(1, 10):
		if isValidPosition(digit, row, col, board):
			# if a valid position, place digit there temporarily until
			# it is proven invalid and we backtrack later
			board[row][col] = digit
			if solvePartialSudoku(row, col + 1, board):
				return True
	# backtrack and mark as empty
	board[row][col] = 0
	return False

def isValidPosition(value, row, col, board):
	# check the row and column validity
	rowIsValid = value not in board[row]
	columnIsValid = value not in map(lambda r: r[col], board)
	
	if not rowIsValid or not columnIsValid:
		return False
	
	# check subgrid
	subgridRowStart = (row // 3) * 3
	subgridColStart = (col // 3) * 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart + rowIdx
			colToCheck = subgridColStart + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				# if an existing value is found, return False
				return False
	
	return True
	