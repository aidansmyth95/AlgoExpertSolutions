'''
I would say find horizontal edges, and vertcal edges.
Then find smallest area between them. This is similar to solution 1.
Solution 2 attempts to draw opposite diagonal to a random pair.
If possible we have a rectangle
'''

# O(n^2) T | O(n) S
def minimumAreaRectangle(points):
    columns = initializeColumns(points)
	minAreaFound = float("inf")
	edgesParallelToYAxis = {}
	
	# sort so vertical edges or columns go from left to right
	sortedColumns = sorted(columns.keys())
	# for each column
	for x in sortedColumns:
		yValues = columns[x]
		# sort from lowest to highest
		yValues.sort()
		
		# get point 2
		for currentIdx, y2 in enumerate(yValues):
			# get point 1
			for previousIdx in range(currentIdx):
				y1 = yValues[previousIdx]
				pointString = str(y1) + ":" + str(y2) #y1:y2 at column x
				
				# if there is a matching vertical edge already found
				if pointString in edgesParallelToYAxis:
					currentArea = (x - edgesParallelToYAxis[pointString]) * \
						(y2 - y1)
					minAreaFound = min(minAreaFound, currentArea)
	
				# override edge to move inwards, no need to keep leftmost edge
				edgesParallelToYAxis[pointString] = x
	
	return minAreaFound if minAreaFound != float("inf") else 0
		
def initializeColumns(points):
	columns = {}
	for point in points:
		x,y = point
		if x not in columns:
			columns[x] = []
		columns[x].append(y)
	return columns
	
