'''
Going up and down
Weird cases happen on perimeter

When we are going down and hit left-most column, update row to go 1 down and update direction
If we are in the last row and going down, we should go right and update direction
If we are going up and hit row 0, we go to right and update direction
If we are going up and hit last column, we go down a row and change direction
'''

# O(n) Y | O(S) S
def zigzagTraverse(array):
    result = []
	height = len(array) - 1
	width = len(array[0]) - 1
	c = 0
	r = 0
	goingDown = True # we start going down
	
	while not isOutOfBounds(r, c, height, width):
		result.append(array[r][c])
		if goingDown:
			# if going down and in first column or going down and at last row
			if c == 0 or r == height:
				goingDown = False
				if r == height:
					# go down a row and start going up
					c += 1
				else :
					r += 1
			else:
				r += 1
				c -= 1
		else:
			# if going up and in first row or going up and in last column
			if r == 0 or c == width:
				goingDown = True
				if c == width:
					# move to right and go down
					r += 1
				else :
					# move down a row and start going down
					c += 1
			else:
				r -= 1
				c += 1
	
	return result


def isOutOfBounds(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width
	
