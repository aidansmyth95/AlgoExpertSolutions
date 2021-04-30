'''
Spaces are required. Case sensitive.
I implemented best case solution here.
n is number of characters, m is haracters in doc, c is unique characters in n
'''

# O(n+m) T | O(c) S
def generateDocument(characters, document):
    # build hash map of characters and their freq
	charFreq = {}
	# O(n)
	for char in characters:
		if char not in charFreq:
			charFreq[char] = 1
		else:
			charFreq[char] += 1

	# loop through document now - O(m)
	for char in document:
		if char not in charFreq:
			return False
		# if none left, return False
		if charFreq[char] <= 0:
			return False
		else:
			charFreq[char] -= 1
	
	return True
	
