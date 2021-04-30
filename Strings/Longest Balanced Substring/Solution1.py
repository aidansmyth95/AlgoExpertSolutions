'''
Brute force is O(n^3) - sub-optimal. Nested for loops. We can do better.
Solution 1: Stack. Should be zero at end.
'''

# O(n) ST
def longestBalancedSubstring(string):
    maxLength = 0
	idxStack = []
	idxStack.append(-1)
	
	for i in range(len(string)):
		if string[i] == "(":
			idxStack.append(i)
		else:
			idxStack.pop()
			if len(idxStack) == 0:
				idxStack.append(i)
			else:
				balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
				currentLength = i - balancedSubstringStartIdx
				maxLength = max(maxLength, currentLength)
	
	return maxLength
				
