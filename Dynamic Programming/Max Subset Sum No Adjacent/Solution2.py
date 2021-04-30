'''
We can use dynamic programming.
Greatest sum of non-adjacent previous items built-up in array.
[7, 10, 12, 7, 9, 14] -> [7, 10, 19, 19, 28, 33]

Formula:
maxSums = max (
		maxSums[i-1],
		maxSums[i-2] + array[i]
	)
	
We can do it without array
'''

#O(N) T | O(1) S
def maxSubsetSumNoAdjacent(array):

	# handle empty array cas
	if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	
	# initialize these values
	prevAdj = array[0]
	prevClosest = max(array[0], array[1])

	for i in range(2, len(array)):
		tmp = max(prevClosest, prevAdj + array[i])
		prevAdj = prevClosest
		prevClosest = tmp
	return prevClosest
