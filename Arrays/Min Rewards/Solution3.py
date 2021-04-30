'''
Solution 3 - Cleanest code.

Idea of expanding doesn't have to happen by starting at local mins.
Iterate twice - left to right and then right to left
R2L: Just compare numbers to what comes before them
L2R: Opposite idea
'''

# O(n) ST
def minRewards(scores):
    rewards = [1 for _ in scores]
	# left to right, starting after stepping in one
	for i in range(1, len(scores)):
		if scores[i] > scores[i - 1]:
			rewards[i] = rewards[i - 1] + 1
	# left to right, starting after stepping in one
	for i in range(len(scores) - 2, -1, -1):
		if scores[i] > scores[i + 1]:
			# max of already rewarded vs new reward
			rewards[i] = max(rewards[i + 1] + 1, rewards[i])
	
	return sum(rewards)