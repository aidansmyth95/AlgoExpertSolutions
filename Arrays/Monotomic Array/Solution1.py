'''
My understanding of monotonic: can be zero change or pos/neg, but not pos & neg.
'''

# O(N) T | O(1) S
def isMonotonic(array):
    prevPosChange = None
	for i in range(0, len(array) - 1):
		# take note of first change: is it pos or neg?
		if array[i+1] - array[i] == 0:
			continue
		elif array[i+1] - array[i] > 0:
				currPosChange = True
		else: # array[i+1] - array[i] < 0:
			currPosChange = False

		# check with prevoius posChange
		if prevPosChange == None:
			prevPosChange = currPosChange
		elif prevPosChange != currPosChange:
			return False
	return True