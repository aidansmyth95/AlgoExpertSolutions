'''
We can do better. We only use last two rows, so can reduce space to O(n)
'''

# O(nk) T | O(n) S
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	
	evenProfits = [0 for d in prices]
	oddProfits = [0 for d in prices]
	
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		if t % 2 == 1:
			currProf = oddProfits
			prevProf = evenProfits
		else:
			currProf = evenProfits
			prevProf = oddProfits
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, prevProf[d - 1] - prices[d - 1])
			currProf[d] = max(maxThusFar + prices[d], currProf[d - 1])
	return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]
