'''
Wrap around having visited every element exactly once
When we land, we move that many steps.
'''

def hasSingleCycle(array):
    numMoves = 0
	# start at index zero
	currentIdx = 0
	while numMoves < len(array):
		if numMoves > 0 and currentIdx == 0:
			return False
		currentIdx = getNextIdx(currentIdx, array)
		numMoves += 1
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	# wrap around forwards
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
