# we can save space in solution 1.2
'''
Solution 2: storing at just two rows
'''
# O(nm*min(n,m)) T | O(min(n,m)^2) S
def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	evenLcs = [[] for _ in range(len(small)+1)]
	oddLcs = [[] for _ in range(len(small)+1)]
	for i in range(1, len(big)+1):
		if i % 2 == 1:
			currentLcs = oddLcs
			previousLcs = evenLcs
		else:
			previousLcs = oddLcs
			currentLcs = evenLcs
			
		for j in range(1, len(small)+1):
			if big[i-1] == small[j-1]:
				currentLcs[j] = previousLcs[j-1] + [big[i-1]]
			else:
				currentLcs[j] = max(previousLcs[j], currentLcs[j-1], key=len)
	return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]

