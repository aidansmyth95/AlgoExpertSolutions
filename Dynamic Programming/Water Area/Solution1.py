'''
Very cool problem but difficult to visualize.
'''

# O(n)T | O(1) S
def waterArea(heights):
    if len(heights) < 2:
		return 0
	
	leftIdx = 0
	rightIdx = len(heights) - 1
	surfaceArea = 0
	leftMax = heights[leftIdx]
	rightMax = heights[rightIdx]
	
	# move the pointers
	while leftIdx < rightIdx:
		# move smaller pillar index in one, updating side max
		# add difference between side max and current height at idx to SA
		if heights[leftIdx] < heights[rightIdx]:
			leftIdx += 1
			leftMax = max(leftMax, heights[leftIdx])
			surfaceArea += leftMax - heights[leftIdx]
		else:
			rightIdx -= 1
			rightMax = max(rightMax, heights[rightIdx])
			surfaceArea += rightMax - heights[rightIdx]
	return surfaceArea
