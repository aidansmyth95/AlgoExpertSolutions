'''
Longest string chain. Dynamic programming question involving memoization and
caching.
A string chain is when you remove a single letter from a string, and it matches
the next string in the chain.

Every string can be the head of its longest string chain. And this only needs
to be computed once.

N strings, lomgest string is length M
'''

# O(N * M^2 * NlogN) T - M^2 for iterating AND rebuilding new smaller string
# O(NM) S - Hash table
def longestStringChain(strings):
    # for every string, imagine the longest string chain that starts with it.
	# Set up every string to point to the next string in its respective longest
	# string chain. Also keep track of the lengths of these longest string
	# chains.
	stringChains = {}
	for string in strings:
		stringChains[string] = {"nextString": "", "maxChainLength": 1}

	# Sort the strings based on their lengths so that when we visit a string
	# as we go left to right, we can already have computed the longest substring
	# of any smaller substrings
	sortedStrings = sorted(strings, key=len)
	for string in sortedStrings:
		findLongestStringChain(string, stringChains)
		
	return buildLongestStringChain(strings, stringChains)

def findLongestStringChain(string, stringChains):
	# try removing every letter to see if the remaining strings form a chain
	for i in range(len(string)):
		smallerString = getSmallerString(string, i)
		if smallerString not in stringChains:
			continue
		tryUpdateLongestStringChain(string, smallerString, stringChains)

def getSmallerString(string, idx):
	return string[0:idx] + string[idx + 1 :]

def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
	smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
	currentStringChainLength = stringChains[currentString]["maxChainLength"]
	# update the string chain only if the smaller string leads to a longer chain
	if smallerStringChainLength + 1 > currentStringChainLength:
		stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
		stringChains[currentString]["nextString"] = smallerString
	
def buildLongestStringChain(strings, stringChains):
	maxChainLength = 0
	chainStartingString = ""

	# for loop to find first string in largest string chain
	for string in strings:
		if stringChains[string]["maxChainLength"] > maxChainLength:
			maxChainLength = stringChains[string]["maxChainLength"]
			chainStartingString = string
	
	# starting at the string found above, build the longest string chain
	ourLongestStringChain = []
	currentString = chainStartingString
	# back track through chain
	while currentString != "":
		ourLongestStringChain.append(currentString)
		currentString = stringChains[currentString]["nextString"]
	
	return [] if len(ourLongestStringChain) == 1 else ourLongestStringChain