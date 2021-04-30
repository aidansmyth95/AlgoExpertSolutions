
# O(N) T, #O(N) S - we are adding pairs, at most 2N chars, to list 2N -> N
def runLengthEncoding(string):
	encodedStr = []
	currRunLen = 1
	currChar = string[0] # handle 1 len str
	for i in range(1, len(string)):
		currChar = string[i]
		prevChar = string[i-1]
		if currChar != prevChar or currRunLen == 9:
			encodedStr.append(str(currRunLen))
			encodedStr.append(prevChar)
			currRunLen = 0
		currRunLen += 1
		
	# handle the last currChar
	encodedStr.append(str(currRunLen))
	encodedStr.append(currChar)
	
	return "".join(encodedStr)
	
