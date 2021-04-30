'''
No concatenations in this version.
'''

# O(nm) ST since no concatenations or storing of LCS
def longestCommonSubsequence(str1, str2):
    # [letters in LCS, len(LCS) , previous i idx, previous j idx]
	lcs = [[[None, 0, None, None] for x in range(len(str1)+1)] \
		   for y in range(len(str2)+1)]
	for i in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if str2[i-1] == str1[j-1]:
				lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1, i-1, j-1]
			else:
				if lcs[i-1][j][1] > lcs[i][j-1][1]:
					lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
				else:
					lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
	return buildSequence(lcs)

def buildSequence(lcs):
	seq = []
	i = len(lcs) - 1
	j = len(lcs[0]) - 1
	while i != 0 and j != 0:
		currentEntry = lcs[i][j]
		if currentEntry[0] is not None:
			seq.append(currentEntry[0])
		i = currentEntry[2]
		j = currentEntry[3]
	return list(reversed(seq))