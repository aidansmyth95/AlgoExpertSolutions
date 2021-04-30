'''
Suffix trie example
'''

# O(b^2 + ns) T | O(b^2 + n) S
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
	return [modifiedSuffixTrie.contains(string) for string in smallStrings]

class ModifiedSuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.populateModifiedSuffixTrieFrom(string)
		
	def populateModifiedSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)
			
	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
			
	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return True
		
		
