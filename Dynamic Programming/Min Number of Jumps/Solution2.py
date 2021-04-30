'''
We can solve faster and using less space.
This is the solution I find easiest too.
We know max reach at any point, so can update
If steps reach 0, we take a jump.
'''

# O(n)T | O(1)S
def minNumberOfJumps(array):
    if len(array) == 1:
		return 0
	
	jumps = 0
	maxReach = array[0]
	stepsLeft = array[0]
	
	for i in range(1, len(array) - 1):
		maxReach = max(maxReach, i + array[i])
		stepsLeft -= 1
		# jump when we run out of steps left
		if stepsLeft == 0:
			jumps += 1
			stepsLeft = maxReach - i
	return jumps + 1
		
