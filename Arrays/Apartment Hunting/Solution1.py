'''
First obvious solution is O(b^2 * r) T
We can do better from a time complexity.
We could precompute values to save us iterations
For loop forwards, finding requirements, and then for loop reversed to update
the req distances.
Then we could take the maximum of the values for all requirements, and that
would be the answer per position - O(br) T
'''

# O(rb^2) T | O(b) S
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float('-inf') for block in blocks]
	# outer blocks for loop
	for i in range(len(blocks)):
		# requirements for loop
		for req in reqs:
			closestReqDistance = float('inf')
			# inner blocks for loop
			for j in range(len(blocks)):
				# if req is found
				if blocks[j][req]:
					# distance from current block i to comparison block j
					closestReqDistance = min(closestReqDistance, getDistance(i, j))
			# update max distances at current block i
			maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
	
	return getIdxAtMinValue(maxDistancesAtBlocks)
		
		
def getDistance(a, b):
	return abs(a - b)

def getIdxAtMinValue(array):
	idxAtMinValue = 0
	minValue = float("inf")
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue