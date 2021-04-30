'''
Naive solution would be O(n^4) - not optimal or an option really.
A quadruplet could be expressed as a pair of number:
	x + y + z + k = p + q, where x + y = p and z + k = q
Turns this into a two-number sum problem.
We can store in a hash table p: [[x, y], ... ]
We cannot use same items twice. We handle this by only adding a pair to the hash
table when we are at its second element.
Next if pair makes up difference with another pair to make target, add them all
to the quadruplet list.
'''

# Avg O(n^2) T - two for loops, mostly constant time ops
# Worst: O(n^3) T - we have bunch of pairs that give same value to iterate
# through during inner for loop.
# O(n^2) S - hash table, worst case scenario
def fourNumberSum(array, targetSum):
    quadruplets = []
	allPairs = {}
	# first pass is useless as we only store when index at second element in
	# the pair. Also, leave room for number after it at end of loop
	
	# pick a an element to start at, leaving room for element after it
	for i in range(1, len(array) - 1):
		# iterate through elements after current element
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			# check if difference is in hash table, if so we have a quadruplet
			if difference in allPairs:
				for pair in allPairs[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		# iterate through elements before current element
		for k in range(i):
			currentSum = array[i] + array[k]
			# append or create new list entry
			if currentSum not in allPairs:
				allPairs[currentSum] = [[array[i], array[k]]]
			else:
				allPairs[currentSum].append([array[i], array[k]])
	return quadruplets
	