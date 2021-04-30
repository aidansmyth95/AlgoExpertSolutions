'''
Start and end time student would like to rent a laptop.
How many laptops does school need to facilitate all students?
'''

def laptopRentals(times):
    if len(times) == 0:
    	return 0

	usedLaptops = 0
	startTimes = sorted([interval[0] for interval in times])
	endTimes = sorted([interval[1] for interval in times])
	
	startIterator = 0
	endIterator = 0
	
	while startIterator < len(times):
		if startTimes[startIterator] >= endTimes[endIterator]:
			usedLaptops -= 1
			endIterator += 1
		usedLaptops += 1
		startIterator += 1

	return usedLaptops