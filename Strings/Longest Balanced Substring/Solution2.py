'''
Solution 2: Go left and count (, the go right and count )
'''

# O(n) T | O(1) S
def longestBalancedSubstring(string):
    return max(getLongestBalancedInDir(string, True),
			  getLongestBalancedInDir(string, False))

def getLongestBalancedInDir(string, leftToRight):
	openingParens = "(" if leftToRight else ")"
	startIdx = 0 if leftToRight else len(string) - 1
	step = 1 if leftToRight else -1
	
	maxLength = 0
	openingCount = 0
	closingCount = 0
	
	idx = startIdx
	while idx >= 0 and idx < len(string):
		char = string[idx]
		
		if char == openingParens:
			openingCount += 1
		else:
			closingCount += 1
		
		if openingCount == closingCount:
			maxLength = max(maxLength, closingCount * 2)
		elif closingCount > openingCount:
			openingCount = 0
			closingCount = 0
		
		idx += step
		
	return maxLength