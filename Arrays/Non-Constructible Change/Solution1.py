'''
Min number of change that you cannot create.
Coins are cents in this case.
Brute force: loop through al pos integers until you cannot create it. This
would be very sub-optimal
'''

# O(nlogn) T
def nonConstructibleChange(coins):
    coins.sort()
	changeCreated = 0
	for coin in coins:
		if coin > changeCreated + 1:
			return changeCreated + 1
		
		changeCreated += coin
	return changeCreated + 1
