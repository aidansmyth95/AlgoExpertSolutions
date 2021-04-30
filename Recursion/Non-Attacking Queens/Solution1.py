'''
No queen can move to position of another queen.
'''

# O(n!) T | O(n) S
def nonAttackingQueens(n):
    # Write your code here.
    columnPlacements = [0] * n
	return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)

def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
	if row == boardSize:
		return 1
	
	validPlacements = 0
	for col in range(boardSize):
		if isNonAttackingPlacement(row, col, columnPlacements):
			columnPlacements[row] = col
			validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)
	return validPlacements

def isNonAttackingPlacement(row, col, columnPlacements):
	for prevRow in range(row):
		colToCheck = columnPlacements[prevRow]
		sameCol = colToCheck == col
		onDiagonal = abs(colToCheck - col) == row - prevRow
		if sameCol or onDiagonal:
			return False
	return True
