'''
FIrst solution is worst one. Recursive, no memoization.

With maxSteps of 2, stairCase height:
0 -> 1 way
1 -> 1 way
2 -> 2 ways
3 -> 3 ways
4 -> 5 ways .... 
h = h-1 + h-2
'''



def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return numberOfWaysToTop(height, maxSteps)

# worst way, no memoization
# O(k^n) T | O(n) S
def numberOfWaysToTop(height, maxSteps):
	if height <= 1:
		return 1
	
	numberOfWays = 0
	for step in range(1, min(maxSteps, height) + 1):
		numberOfWays += numberOfWaysToTop(height - step, maxSteps)
	
	return numberOfWays
	
# with memoization
# O(n * k) T | O(n) S
def numberOfWaysToTopWithMem(height, maxSteps, memoize={0: 1, 1: 1}):
	if height in memoize:
		return memoize[height]
	
	numberOfWays = 0
	for step in range(1, min(maxSteps, height) + 1):
		numberOfWays += numberOfWaysToTop(height - step, maxSteps)
		
	memoize[height] = numberOfWays
	
	return numberOfWays
