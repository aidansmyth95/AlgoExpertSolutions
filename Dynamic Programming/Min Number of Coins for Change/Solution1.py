'''
Dynamic programming: Build up solution by building up solutions to smaller
problems

Go one denom at a time.

If denom <= i:
	n - denom = x
	x is y coins
	denom is 1 coin
	x + denom = new value

if denom <= amount:
	nums[amount] = min(nums[amount], 1 + nums[amount-denom])

0
0 1 2 3 4 5 6
0 1 1 2 2 3 3
0 1 1 2 1 2 2
_ _ _ _ _ _ _ ($)

'''

# O(nd) T | O(n) S
def minNumberOfCoinsForChange(n, denoms):
	
	nums = [float("inf") for i in range(n + 1)]
	nums[0] = 0
	for denom in denoms:
		for amount in range(n + 1):
			if denom <= amount:
				nums[amount] = min(nums[amount], 1 + nums[amount - denom])
				
	return nums[n] if nums[n] != float("inf") else -1

