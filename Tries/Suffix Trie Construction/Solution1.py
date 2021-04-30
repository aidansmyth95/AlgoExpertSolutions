'''
A simpler data structure than a suffix tree.
Ends with "*"
Build using hash tables. Every node is a key, pointing to another hash table.

Bottom nodes point to empty hash tables, "*"
Check whether current letter is already stored in tree.
	If not, add a key that points to another empty hash table.
	If yes, move to already existing hash table.
Move node down suffix, repeating. At end, add "*".
Then go back to root and repeat for next process.

Efficient way to store lots of suffixes at it grows.
'''


# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	# O(n^2) T | O(n^2) S - all the suffices and all their characters (n^2)
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)
			
	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True
		
	# O(m) T | O(1) S - where m is length of string we are searching for
    def contains(self, string):
        node = self.root
		for letter in string:
			if letter not in node:
				return False
			# move node
			node = node[letter]
		# true if at end
		return self.endSymbol in node
