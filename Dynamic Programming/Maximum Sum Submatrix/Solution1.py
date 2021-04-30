'''
Consider all submatrices of size x size, and return max sum of it.
Brute force: O(w * h * size^2) -> we can do better.
Solution: use a space to store sums that we have already calculated
'''

# O(wh) ST
def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
	maxSubMatrixSum = float("-inf")
	
	for row in range(size - 1, len(matrix)):
		for col in range(size - 1, len(matrix[row])):
			total = sums[row][col]
			touchesTopBorder = row - size < 0
			if not touchesTopBorder:
				total -= sums[row - size][col]
			
			touchesLeftBorder = col - size < 0
			if not touchesLeftBorder:
				total -= sums[row][col - size]
				
			touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
			if not touchesTopOrLeftBorder:
				total += sums[row - size][col - size]
				
			maxSubMatrixSum = max(maxSubMatrixSum, total)
		
	return maxSubMatrixSum
				
				
def createSumMatrix(matrix):
	sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
	sums[0][0] = matrix[0][0]
	
	for idx in range(1, len(matrix[0])):
		sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
		
	for idx in range(1, len(matrix)):
		sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
		
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - \
								sums[row - 1][col - 1] + matrix[row][col]
	
	return sums
