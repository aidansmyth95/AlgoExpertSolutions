'''
Reach a target between low and high using imprecise measuring cups.
Lends itself very well to recursion, with memoization.
'''

# O(low * high * n) T | O(low * high) S
def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
	return canMeasureInRange(measuringCups, low, high, memoization)

def canMeasureInRange(measuringCups, low, high, memoization):
	memoizeKey = createHashTableKey(low, high)
	if memoizeKey in memoization:
		return memoization[memoizeKey]
	
	if low <= 0 and high <= 0:
		return False
	
	canMeasure = False
	for cup in measuringCups:
		cupLow, cupHigh = cup
		if low <= cupLow and cupHigh <= high:
			canMeasure = True
			break
		
		newLow = max(0, low - cupLow)
		newHigh = max(0, high - cupHigh)
		canMeasure = canMeasureInRange(measuringCups, newLow, newHigh, memoization)
		if canMeasure:
			break

	memoization[memoizeKey] = canMeasure
	return canMeasure
	
def createHashTableKey(low, high):
	return str(low) + ":" + str(high)
