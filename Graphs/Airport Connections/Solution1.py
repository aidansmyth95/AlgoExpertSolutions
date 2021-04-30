'''
Min number of airport stops.
In this case, some airports are more valuable than others.
Some at top of chain unlock more mairports downstream in graph than others.

Find unreachable airports, give score based on airports they unlock, add stop,
remove unlocked airports from list, continue and repeat until all airports are
unlocked.

DFS to find downstream airport nodes.
'''

# O(a * (a + r) + alog(a)) T | O(a + r) S
def airportConnections(airports, routes, startingAirport):
	airportGraph = createAirportGraph(airports, routes)
	unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
	markUnreachableConnections(airportGraph, unreachableAirportNodes)
	return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)

# O(a + r) ST
def createAirportGraph(airports, routes):
	airportGraph = {}
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	for route in routes:
		airport, connection = route
		airportGraph[airport].connections.append(connection)
	return airportGraph

# (a + r) T | O(a) S
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
	# DFS from starting airport and then see which ones we do not reach
	visitedAirports = {}
	depthFirstSearchAirports(airportGraph, startingAirport, visitedAirports)
	unreachableAirportNodes = []
	for airport in airports:
		if airport in visitedAirports:
			continue
		airportNode = airportGraph[airport]
		airportNode.isReachable = False
		unreachableAirportNodes.append(airportNode)
	return unreachableAirportNodes

def depthFirstSearchAirports(airportGraph, airport, visitedAirports):
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstSearchAirports(airportGraph, connection, visitedAirports)

# O( a * (a + r)) T worst case scenario. | O(a) S
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {})
		airportNode.unreachableConnections = unreachableConnections

def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
	if airportGraph[airport].isReachable:
		return
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	unreachableConnections.append(airport)
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstAddUnreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)

# O(alog(a) + a + r) T | O(1) S
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
	# sort by score - num unreachable connections
	unreachableAirportNodes.sort(key = lambda airport: len(airport.unreachableConnections), reverse=True)
	numNewConnections = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numNewConnections += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return numNewConnections
	
class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []
		
