'''
Red shirts in same row, blue shirts in same row
Front row must be shorter than back row
True if possible to take photo
'''

# O(nlog(n)) T | O(1) S
def classPhotos(redShirtHeights, blueShirtHeights):
    # determine which colour shirts in which row.
	# we do this by looking at tallenst student - reverse sort
	# sort students
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	backRow = 'RED'
	if redShirtHeights[0] < blueShirtHeights[0]:
		backRow = 'BLUE'

	# then a for loop to make sure photo is possible:
	for i in range(len(redShirtHeights)):
		if backRow == 'RED':
			if redShirtHeights[i] <= blueShirtHeights[i]:
				return False
		else:
			if blueShirtHeights[i] <= redShirtHeights[i]:
				return False
	return True