'''
Infinite number of coins at our disposal
How many ways can we make it with 1s

For each denom:
If the denom is less than the amount, update amout with a count

n=10 denom=[1,5,10,25]

1 1 1 1 1 1 1 1 1 1
then
1 1 1 1 1 2 2 2 2 2
then
1 1 1 1 1 2 2 2 2 3
and +1 at end gives 4
'''

def numberOfWaysToMakeChange(n, denoms):
    print('\n{} made with {}'.format(n, str(denoms)))
	ways = [0 for val in range(n + 1)]
	ways[0] = 1 # there is 1 way to make 0
	for denom in denoms:
		print('\tFinding ways for denom {} ...'.format(denom))
		for amount in range(1, n+1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
		print('\tways: {}'.format(str(ways)))
	print('Answer: {} ways'.format(ways[n]))
	return ways[n]
