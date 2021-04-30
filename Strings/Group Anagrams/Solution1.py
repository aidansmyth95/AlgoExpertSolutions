'''
We can sort word and create entry in Hash table.
w words, n is character length of longest word.
Sorting takes n * log(n) Time, and we do for w words
'''

# O(w * n * log(n)) | O(w * n) S
def groupAnagrams(words):
    anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			# we already have an entry. Append original word to it
			anagrams[sortedWord].append(word)
		else:
			# make a new entry
			anagrams[sortedWord] = [word]
	return list(anagrams.values())
