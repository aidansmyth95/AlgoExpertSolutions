'''
Arbitrage: Profit after N exchanges
Model it as a graph: currencies are vertices, edges are exchange rates.
All edges are directed.
A cycle that ends & multiplies out to > 1.0 is an arbitrage found!
Bellman Ford algorithm determines negative-weight cycle. Modify this algorithm.
Take negative logirthm of ERs to do this inversion.
If log(a) + log(b) < 0 we have arbitrage.
'''
import math

# O(n^3) T | O(n^2) S
def detectArbitrage(exchangeRates):
    logExchangeRates = convertToLogMatrix(exchangeRates)
	
	return foundNegativeWeightCycle(logExchangeRates, 0)

def convertToLogMatrix(matrix):
	newMatrix = []
	for row, rates in enumerate(matrix):
		newMatrix.append([])
		for rate in rates:
			newMatrix[row].append(-math.log10(rate))
	return newMatrix
	
def foundNegativeWeightCycle(graph, start):
	distancesFromStart = [float("inf") for _ in range(len(graph))]
	distancesFromStart[start] = 0
	
	for _ in range(len(graph) - 1):
		if not relaxEdgesAndUpdateDistances(graph, distancesFromStart):
			return False
	return relaxEdgesAndUpdateDistances(graph, distancesFromStart)

def relaxEdgesAndUpdateDistances(graph, distances):
	updated = False
	for sourceIdx, edges in enumerate(graph):
		for destinationIdx, edgeWeight in enumerate(edges):
			newDistanceToDestination = distances[sourceIdx] + edgeWeight 
			if newDistanceToDestination < distances[destinationIdx]:
				updated = True
				distances[destinationIdx] = newDistanceToDestination
	return updated
