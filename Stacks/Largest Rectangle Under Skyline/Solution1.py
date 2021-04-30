'''
Array of building heights. Return area of largest rectangle of adjacent buildings.
Use stack to improve time complexity.
Loop through all building, compare to height of buildings on top of stack.
I
'''

# O(n) ST
def largestRectangleUnderSkyline(buildings):
    pillarIndices = []
	maxArea = 0
	
	for idx, height in enumerate(buildings + [0]):
		while len(pillarIndices) != 0 and \
			buildings[pillarIndices[len(pillarIndices) - 1]] >= height:
			
			pillarHeight = buildings[pillarIndices.pop()]
			width = idx if len(pillarIndices) == 0 else \
				idx - pillarIndices[len(pillarIndices) - 1] - 1
			maxArea = max(width * pillarHeight, maxArea)
			
		pillarIndices.append(idx)
		
	return maxArea
