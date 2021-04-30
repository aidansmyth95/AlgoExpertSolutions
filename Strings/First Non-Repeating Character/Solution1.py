'''
Obvious soln is the O(n^2) double for loop, but we can do better
Hash map. And since we only have 26 characters, this is O(1) size!
'''

# O(n) T | O(1) S
def firstNonRepeatingCharacter(string):
    charFreq = {}
	
	# for loop of string char to build charFreq - O(n) T
	for character in string:
		# increment frequency in hash map
		charFreq[character] = charFreq.get(character, 0) + 1
		
	# for loop of 26 chars in hash map - O(1) T
	for idx in range(len(string)):
		character = string[idx]
		if charFreq[character] == 1:
			return idx
		
	return -1
