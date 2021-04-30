'''
Real life applications like this job task question
First job is a prereq for next job.

Topological sort describes a directed graph, and is a linear ordering of
the vertices of the graph so long as x comes before y in the ordering.
Has to be a directed acyclic graph - no cycles.

Keep track of visited and nodes in progress of visiting.

We draw directed edges in our graph from x to y.

Prerequisites exist if node has arrow pointing towards it.
Grab a random node. We want to add nodes that do not have prereq or all prereq
have to be complete

SOln 1: DFS
Soln 2: modify graph

'''

# O(J+D) ST
def topologicalSort(jobs, deps):
    jobGraph = createJobsGraph(jobs, deps)
	return getOrderedJobs(jobGraph)

def createJobsGraph(jobs, deps):
	graph = JobGraph(jobs)
	# populate the prerequisites to graph - adding edges
	for prereq, job in deps:
		graph.addPrereq(job, prereq)
	return graph

def getOrderedJobs(graph):
	orderedJobs = []
	nodes = graph.nodes
	while len(nodes):
		node = nodes.pop()
		# traverse nodes in DFS way, adding jobs to orderedJobs, checking for
		# any existing cycles
		containsCycle = depthFirstTraverse(node, orderedJobs)
		if containsCycle:
			return []
	return orderedJobs

def depthFirstTraverse(node, orderedJobs):
	if node.visited:
		# we have nothing to do
		return False
	if node.visiting:
		return True
	node.visiting = True
	for prereqNode in node.prereqs:
		# do same thing for prereq nodes
		containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
		if containsCycle:
			return True
	# node is now visited
	node.visited = True
	node.visiting = False
	orderedJobs.append(node.job)
	return False

class JobGraph:
	def __init__(self, jobs):
		self.nodes = [] # list of nodes
		self.graph = {} # define actual graph mapping of integer jobs to nodes
		for job in jobs:
			self.addNode(job)
	
	def addPrereq(self, job, prereq):
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prereq)
		jobNode.prereqs.append(prereqNode)
		
	def addNode(self, job):
		self.graph[job] = JobNode(job)
		self.nodes.append(self.graph[job])
		
	def getNode(self, job):
		# if job not in graph, add it
		if job not in self.graph:
			self.addNode(job)
		return self.graph[job]
		
class JobNode:
	def __init__(self, job):
		self.job = job
		self.prereqs = []
		self.visited = False
		self.visiting = False