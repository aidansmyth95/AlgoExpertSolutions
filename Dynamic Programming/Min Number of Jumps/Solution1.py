'''
Famous problem.
First solution I find less intuitive.
Seems to be a dynamic programming one.
Involves less code
Build array of min number of jumps to go from first idx to curr idx
'''

# O(n^2) T | O(n) S
def minNumberOfJumps(array):
    jumps = [float("inf") for x in array]
	jumps[0] = 0
	for i in range(1, len(array)):
		for j in range(0, i):
			if array[j] >= i - j:
				jumps[i] = min(jumps[j]+1, jumps[i])
	return jumps[-1]
