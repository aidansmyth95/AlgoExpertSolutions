def smallestDifference(arrayOne, arrayTwo):
    # sort both arrays
	# for loop one array, and assign left/right pointers to the other one.
	# move pointers to find min difference and update the pair if
	# it is less than existing min diff pair.
	
	# default values to start
	minDiff = abs(arrayOne[0] - arrayTwo[0])
	minPair = [arrayOne[0], arrayTwo[0]]
	
	# sort both arrays
	arrayOne.sort()
	arrayTwo.sort()
	
	idxOne = 0
	idxTwo = 0
	minPair = [arrayOne[idxOne], arrayTwo[idxTwo]]
	minAbsDiff = float("inf")
	
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
    	valOne = arrayOne[idxOne]
		valTwo = arrayTwo[idxTwo]
		currAbsDiff = abs(valOne - valTwo)

		
		if currAbsDiff < minAbsDiff:
			minAbsDiff = currAbsDiff
			minPair = [valOne,  valTwo]

		# we move first idx if first num < second num
		if valOne < valTwo:
			idxOne += 1
		# vice versa
		elif valOne > valTwo:
			idxTwo += 1
		# return as we cant do better than 0 diff
		else:
			return [valOne,  valTwo]
		
	return minPair
