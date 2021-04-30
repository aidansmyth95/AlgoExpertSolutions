# O(nlogn) T | O(n) S
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
	mergedIntervals = []
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)
	
	# append interval and keep reference to it - saves time
	# merge is just updating end time of current reference
	for nextInterval in sortedIntervals:
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval
		
		if currentIntervalEnd >= nextIntervalStart:
			# there is an overlap
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		else:
			# there is no overlap
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
	return mergedIntervals
			