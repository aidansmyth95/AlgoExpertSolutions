'''
Greedy algorithm
Take longest and shorted
We need to sort to do this
We need to keep track of indices
'''

# O(nlogn) T | O(n) S
def taskAssignment(k, tasks):
    assignedTasks = []
	originalTasks = getTaskDurationToIdx(tasks)
	sortedTasks = tasks.sort()
	
	# now to implement greedy search min & max pairing
	for k in range(len(tasks) // 2):
		minTask = tasks[k]
		maxTask = tasks[-1-k]
		origIdxMinTask = originalTasks[minTask].pop()
		origIdxMaxTask = originalTasks[maxTask].pop()
		assignedTasks.append([origIdxMinTask, origIdxMaxTask])
	
    return assignedTasks

def getTaskDurationToIdx(tasks):
	taskIdx = {}
	for idx, task in enumerate(tasks):
		# check if already an entry is dict, add new entry if not
		if task in taskIdx:
			taskIdx[task].append(idx)
		else:
			taskIdx[task] = [idx]
	return taskIdx