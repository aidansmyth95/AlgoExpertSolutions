'''
Very famous problem. Capacity is weight that the bag can cary.
2nd int value is weight, 1st value represents the monetary value of item.
Dynamic programming.
2D array of greatest values in knapsack, but with some restrictions

		0	1	2	3	4	5	6	7	8	9	10	-> bags of capacity...
[]		0	0	0	0	0	0	0	0	0	0	0
[1,2]	0	0	1	1	1	1	1	1	1	1	1
[4,3]	0	0	1	4	4	5	5	5	5	5	5
[5,6]	0	0	1	4	4	5	5	5	6	9	9
[6,7]	0	0	1	4	4	5	5	6	6	9	10 -> answer is 10
^
values up to and including ...
What was value of row above minus weight in cols

if w <= j
	value[i][j] = max(value[i-1][j], value[i-1][j-w]+v)
else
	value[i][j] = value[i-1][j]
'''

# O(nc) ST
def knapsackProblem(items, capacity):
	ksValues = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
	for i in range(1, len(items) + 1):
		currW = items[i-1][1]
		currV = items[i-1][0]
		for c in range(capacity+1):
			if currW > c:
				ksValues[i][c] = ksValues[i-1][c]
			else:
				ksValues[i][c] = max(ksValues[i-1][c], ksValues[i-1][c-currW] + currV)
	return [ksValues[-1][-1], getKsItems(ksValues, items)]
	
def getKsItems(ksValues, items):
	seq = []
	i = len(ksValues) - 1
	c = len(ksValues[0]) - 1
	while i > 0:
		if ksValues[i][c] == ksValues[i-1][c]:
			i -= 1
		else:
			seq.append(i-1)
			c -= items[i-1][1]
			i -= 1
		if c == 0:
			break
	return list(reversed(seq))