'''
Recreate opposite diagonal.
'''

# O(n^2) T | O(n) S
def minimumAreaRectangle(points):
    pointSet = createPointSet(points)
	minAreaFound = float("inf")
	
	for currentIdx, p2 in enumerate(points):
		p2x, p2y = p2
		for previousIdx in range(currentIdx):
			p1x, p1y = points[previousIdx]
			
			# skip if shared point - it would just find itself
			pointsShareValue = p1x == p2x or p1y == p2y
			if pointsShareValue:
				continue
				
			# if the points (p1x, p2y) and (p2x, p1y) exit - we have rectangle
			p1DiagExist = convertPointToString(p1x, p2y) in pointSet
			p2DiagExist = convertPointToString(p2x, p1y) in pointSet
			oppositeDiagExist = p1DiagExist and p2DiagExist
			
			if oppositeDiagExist:
				area = abs(p2x - p1x) * abs(p2y - p1y)
				minAreaFound = min(area, minAreaFound)
	
	return minAreaFound if minAreaFound != float("inf") else 0

def createPointSet(points):
	pointSet = set()
	for p in points:
		x, y = p
		pStr = convertPointToString(x, y)
		pointSet.add(pStr)
	return pointSet

def convertPointToString(a, b):
	return str(a) + ":" + str(b)