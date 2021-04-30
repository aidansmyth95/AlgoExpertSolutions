'''
My Solution: make list of non-whitespaced words, and then recreate
'''
# O(n) ST - where n is length of string
def reverseWordsInString(string):
    words = []
	for word in string.split(" "):
		words.insert(0, word)
	reversed_string = " ".join(words)

	return reversed_string

