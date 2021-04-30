'''
Dynamic programming, but surprisingly easy!
Sum at previous number + some value, or just restart with new value

3 5 -9 1 3 -2 3 4 7  2 -9 6  3  1  -5 4

3 8 -1 1 4  2 5 9 16 18 9 15 18 19 14 18
Max so far was 19, answer
'''

# O(N) T | O(1) S
def kadanesAlgorithm(array):
	# max so far
	maxSoFar = array[0]
	# running sum
	maxEndingHere = array[0]
	for i in range(1, len(array)):
		num = array[i]
		# update running sum
		maxEndingHere = max(num, maxEndingHere + num)
		# update max so far
		maxSoFar = max(maxSoFar, maxEndingHere)
		
	return maxSoFar