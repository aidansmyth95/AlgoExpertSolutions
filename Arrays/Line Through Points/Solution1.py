'''
Brute force: n^3 time. Not optimal. O(n^2) lines then check n points if they lie
on the line.

slope = rise/run

Solution: check all lines, but not all points necessarily. We are comparing
number of lines that match. Data structure stores slopes of lines that we have
created with a point

{'slope' : num_points}. num_points starts at 2. Increment num_points.

'''

# O(n^2) T | O(n) S
def lineThroughPoints(points):
    numberOfPointsOnLine = 1
	
	for idx1, p1 in enumerate(points):
		slopes = {}
		for idx2 in range(idx1 + 1, len(points)):
			p2 = points[idx2]
			rise, run = getSlopeBetweenPts(p1, p2)
			# solve floating point slope as key
			slopeKey = createHashTableRational(rise, run)
			if slopeKey not in slopes:
				slopes[slopeKey] = 1
			slopes[slopeKey] += 1
		# default if no values in slopes
		numberOfPointsOnLine = max(numberOfPointsOnLine, max(slopes.values(), default=0))
	return numberOfPointsOnLine


def getSlopeBetweenPts(p1, p2):
	p1x, p1y = p1
	p2x, p2y = p2
	slope = [1, 0] # vertical line slop
	
	# if not vertical line
	if p1x != p2x:
		xDiff = p1x - p2x
		yDiff = p1y - p2y
		gcd = greatestCommonDivisor(abs(xDiff), abs(yDiff))
		xDiff = xDiff // gcd
		yDiff = yDiff // gcd
		if xDiff < 0:
			xDiff *= -1
			yDiff *= -1
		slope = [yDiff, xDiff]
		
	return slope


def createHashTableRational(rise, run):
	return str(rise) + ":" + str(run)

def greatestCommonDivisor(num1, num2):
	a = num1
	b = num2
	while True:
		if a == 0:
			return b
		if b == 0:
			return a
		
		a, b = b, a % b
	