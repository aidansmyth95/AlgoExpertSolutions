'''
We can use a smaller space as we do not use all of edits...
This is very difficult
'''

# O(NM) T | O(min(N,M)) S (smallest string on y axis))
def levenshteinDistance(str1, str2):
	small_str = str1 if len(str1) < len(str2) else str2
	big_str = str1 if len(str1) >= len(str2) else str2

	evenEdits = [x for x in range(len(small_str) + 1)]
	oddEdits = [None for x in range(len(small_str) + 1)]
	
	# set coulumns to be 0 - len(str2)
	for i in range(1, len(big_str) + 1):
		if i % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits
		
		# row number
		currentEdits[0] = i
		# now nested for loops...
		for j in range(1, len(small_str) + 1):
			# and formula...
			if big_str[i-1] == small_str[j-1]:
				currentEdits[j] = previousEdits[j - 1]
			else:
				currentEdits[j] = 1 + min(
					previousEdits[j - 1],
					previousEdits[j],
					currentEdits[j - 1])

	return evenEdits[-1] if len(big_str) % 2 == 0 else oddEdits[-1]