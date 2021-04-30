'''
Solution 2. There are trends, a linear graph with local min.
Go to local min, expand and increment rewards from there until reach a peak.
So we just need to find local mins
'''

# O(n) ST
def minRewards(scores):
    rewards = [1 for _ in scores]
	localMinIdxs = getLocalMinIdxs(scores)
	for local in localMinIdxs:
		expandFromLocalMinIdx(local, scores, rewards)
	return sum(rewards)

def getLocalMinIdxs(array):
	if len(array) == 1:
		return [0]
	localMinIdxs = []
	for i in range(len(array)):
		# corener cases for extremities
		if i == 0 and array[i] < array[i + 1]:
			localMinIdxs.append(i)
		if i == len(array) - 1 and array[i] < array[i - 1]:
			localMinIdxs.append(i)
		if i == 0 or i == len(array) - 1:
			# we have already appended these cases, skip next bit
			continue
		# append local min
		if array[i] < array[i + 1] and array[i] < array[i - 1]:
			localMinIdxs.append(i)
	return localMinIdxs
		
def expandFromLocalMinIdx(idx, array, rewards):
	leftIdx = idx - 1
	# find peak to left
	while leftIdx >= 0 and array[leftIdx] > array[leftIdx + 1]:
		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
		leftIdx -= 1
	rightIdx = idx + 1
	# find peak to right
	while rightIdx < len(array) and array[rightIdx] > array[rightIdx - 1]:
		# when moving right we know that there is no need for max, as it has
		# not already been rewarded
		rewards[rightIdx] = rewards[rightIdx - 1] + 1
		rightIdx += 1