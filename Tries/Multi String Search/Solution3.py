'''
Trie example
'''

# O(bs + ns) T | O(ns) S
def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
	containedStrings = {}
	for i in range(len(bigString)):
		findSmallStringsIn(bigString, i, trie, containedStrings)
	return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
	node = trie.root
	for i in range(startIdx, len(string)):
		char = string[i]
		if char not in node:
			break
		node = node[char]
		if trie.endSymbol in node:
			containedStrings[node[trie.endSymbol]] = True

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def insert(self, string):
		node = self.root
		for j in range(len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = string