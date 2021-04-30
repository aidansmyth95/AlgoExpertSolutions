'''
Start at top right. Look down. Look left. Move idx if not found.
'''
# O(n+m) T | O(1) S
def searchInSortedMatrix(matrix, target):
	# starting at top right
	col = len(matrix[0]) - 1
	row = 0
	while col >= 0 and row <= len(matrix):
		# look down
		if matrix[row][col] == target:
			return [row, col]
		elif matrix[row][col] < target:
			row += 1
		else:
			# > target
			col -= 1
	return [-1, -1]


'''
Worst scenario is O(n*m)T, very naive
'''
def searchNaivelyInSortedMatrix(matrix, target):
    # nested for loops
	num_rows = len(matrix)
	num_cols = len(matrix[0])
	
	for row in range(num_rows):
		for col in range(num_cols):
			if matrix[row][col] == target:
				return [row, col]
			elif matrix[row][col] > target:
				break
	
	return [-1, -1]
