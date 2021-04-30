'''
Populate fraactions of water in each row, until we reach buckets.
Water starts as -1 units, since first row does not matter.
Water does not bounce off wall if it goes out of bounds.
Blocks have value 1
'''

# O(W * W * H) T | O(W) S
def waterfallStreams(array, source):
    rowAbove = array[0][:] # make copy of first row
	rowAbove[source] = -1 # water source is -1

	for row in range(1, len(array)):
		# make copy of row
		currRow = array[row][:]
		
		for idx in range(len(rowAbove)):
			valueAbove = rowAbove[idx]
			hasWaterAbove = valueAbove < 0
			hasBlock = currRow[idx] == 1
			
			if not hasWaterAbove:
				# do nothing if no water above
				continue
				
			if not hasBlock:
				# move water down
				currRow[idx] += valueAbove
				continue
			
			# split water left & right
			splitWater = valueAbove / 2
			
			rightIdx = idx # right pointer
			while rightIdx + 1 < len(rowAbove):
				# move water right
				rightIdx += 1
				if rowAbove[rightIdx] == 1:
					# if block above, we are blocked from water
					break
				if currRow[rightIdx] != 1:
					# if not a block
					currRow[rightIdx] += splitWater
					break
					
				# then do same with left
			leftIdx = idx # right pointer
			while leftIdx > 0:
				# move water right
				leftIdx -= 1
				if rowAbove[leftIdx] == 1:
					# if block above, we are blocked from water
					break
				if currRow[leftIdx] != 1:
					# if not a block
					currRow[leftIdx] += splitWater
					break

		rowAbove = currRow
		
	# convert from negative decimals to %
	finalPctg = list(map(lambda k: k * -100, rowAbove))
	return finalPctg
					