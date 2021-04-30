# O(br) T | O(br) S
def apartmentHunting(blocks, reqs):
	# precompute maxDistancesFromBlocks
	# map each requirement to minDistances
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
	# then get max distances of req at each block
	maxDistancesFromBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
	return getIdxAtMinValue(maxDistancesFromBlocks)
	
def getMinDistances(blocks, req):
	minDistances = [0 for block in blocks]
	closestReqIdx = float("inf") # in this direction...
	# iterate left to right
	for i in range(len(blocks)):
		# if requirement present at current block
		if blocks[i][req]:
			closestReqIdx = i
		minDistances[i] = getDistance(i, closestReqIdx)
	# pass right to left
	for i in reversed(range(len(blocks))):
		# if requirement present at current block
		if blocks[i][req]:
			closestReqIdx = i
		# update minDistances if right to left distance is smaller
		minDistances[i] = min(minDistances[i], getDistance(i, closestReqIdx))
	return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
	# find max distances from all min distances of blocks
	maxDistancesAtBlocks = [0 for b in blocks]
	for i in range(len(blocks)):
		minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
		maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
	return maxDistancesAtBlocks
		
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