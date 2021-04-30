'''
Brute force solution
'''

# O(n^2) T | O(1) S
def validStartingCity(distances, fuel, mpg):
	numberOfCities = len(distances)
	
	for startCity in range(numberOfCities):
		milesRemaining = 0
		for currentCity in range(startCity, startCity + numberOfCities):
			if milesRemaining < 0:
				continue
				
			currentCity = currentCity % numberOfCities
			fuelFromCurrentCity = fuel[currentCity]
			distanceToNextCity = distances[currentCity]
			milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity
			
		# if after looping through all cities we have made it
		if milesRemaining >= 0:
			return startCity
	return -1
			