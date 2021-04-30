'''
Smarter answer:
Answer is the city that we enter with the least amount of gas in tank.
'''

# O(N) T | O(1) S
def validStartingCity(distances, fuel, mpg):
    numCities = len(distances)
	startingCity = 0
	# start at city 0, and set it to have 0 fuel in tank
	minEnteringGas = 0
	enteringGas = 0
	for currentCity in range(1, numCities):
		enteringGas += fuel[currentCity - 1] * mpg - distances[currentCity - 1]
		if enteringGas < minEnteringGas:
			minEnteringGas = enteringGas
			startingCity = currentCity
	return startingCity
	
	
	
    return -1
