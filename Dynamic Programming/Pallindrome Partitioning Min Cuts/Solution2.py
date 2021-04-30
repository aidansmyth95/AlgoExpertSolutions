'''
We can eliminate call of isPalindrome, using dynamic programming tactics.
'''

# O(n^2) T | O(n^2) S
def palindromePartitioningMinCuts(string):
    palindromes = [[False for i in string] for j in string]
	for i in range(len(string)):
		# diagonal is always palindrome
		palindromes[i][i] = True
	# substring length
	for length in range(2, len(string) + 1):
		for i in range(0, len(string) - length + 1):
			j = i + length - 1
			if length == 2:
				# easy check for substring length 2
				palindromes[i][j] = string[i] == string[j]
			else:
				palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]
	# then cuts
	cuts = [float("inf") for i in string]
	for i in range(len(string)):
		if palindromes[0][i]:
			cuts[i] = 0
		else:
			# add a cut, tentatively
			cuts[i] = cuts[i - 1] + 1
			# then iterate & check after tentative cut
			for j in range(1, i):
				if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
					# update if a palindrome found
					cuts[i] = cuts[j - 1] + 1
	return cuts[-1]