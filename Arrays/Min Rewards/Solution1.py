'''
Solution 1: More naive approach.
Iterate through scores.
When greater then prev, incr reward
If smaller, iterate back and fix everybody
'''
# O(n^2) T | O(n) S
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		j = i - 1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j + 1]:
				# we might want to fix previous value, or we might not
				# it should be maximum of what it previously had, or prev+1
				rewards[j] = max(rewards[j], rewards[j + 1] + 1)
				j -= 1
	return sum(rewards)


''' My initial attempt, passes 7/9 tests ...
def minRewards(scores):
    rewards = [False for _ in scores]
	numRewarded = 0
	
	while numRewarded < len(scores):
		# find the minimum unrewarded student
		minScore = float("inf")
		minIdx = -1
		for i in range(len(scores)):
			if not rewards[i]:
				# if not already rewarded
				if scores[i] < minScore:
					minScore = scores[i]
					minIdx = i
		# min element gets reward of 1
		rewards[minIdx] = 1
		numRewarded += 1
		# build up rewards either side of them until change in trend
		leftIdx = minIdx - 1
		rightIdx = minIdx + 1
		while leftIdx >= 0:
			# check if already rewarded
			if rewards[leftIdx]:
				break
			if scores[leftIdx] < scores[leftIdx + 1]:
				# if change in trend, break while loop
				break
			rewards[leftIdx] = minIdx - leftIdx + 1
			numRewarded += 1
			leftIdx -= 1
		while rightIdx < len(scores):
			# check if already rewarded
			if rewards[rightIdx]:
				break
			if scores[rightIdx] < scores[rightIdx - 1]:
				# if change in trend, break while loop
				break
			rewards[rightIdx] = rightIdx - minIdx + 1
			numRewarded += 1
			rightIdx += 1
			
	# one last loop to make sure no matching values
	for i in range(1, len(scores)):
		if rewards[i] == rewards[i-1]:
			rewards[i-1] += 1

	print(scores)
	print(rewards)
	return sum(rewards)
'''		
