'''
Dynamic programming.
Array is price of stock at different days. K is amount of transactions you
can do. We can only hold one share at a time.
Buy low, sell high ;-)

Build 2D array: columns are prices and rows are transactions
prices=[5, 11, 3, 50, 60, 90], k=2

0	0	0	0	0	0	0
1	0	6	6	47	57	87
2	0	6	6	53	63	93	answer is 93

profit[t][d] = max(profit[t][d-1], prices[d] + max(-prices[x]+profit[t-1][x])
where 0 <= x < d
'''

# O(nk) ST
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	profits = [[0 for d in prices] for t in range(k + 1)]
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
			profits[t][d] = max(maxThusFar + prices[d], profits[t][d - 1])
	return profits[-1][-1]
