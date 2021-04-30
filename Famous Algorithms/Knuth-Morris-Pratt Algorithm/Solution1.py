'''
Checks if substring is in string.
Goes from O(nm) T to O(n+m) T
We don't need to recheck already matched patterns. We don't need to go back
to start of substring, we can just go back to last index where we have a 
matching pattern.

Is substring when j reaches end when we compare both strings.
'''

# O(n+m) T | O(m) S
def knuthMorrisPrattAlgorithm(string, substring):
    # get patterns from substring
	pattern = buildPattern(substring)
	return doesMatch(string, substring, pattern)

def buildPattern(substring):
	pattern = [-1 for i in substring]
	j = 0
	i = 1
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j # previous time pattern was found
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return pattern

def doesMatch(string, substring, pattern):
	i = 0
	j = 0
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return False
		
