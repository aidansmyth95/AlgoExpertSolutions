# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	# we can use for loop instead of while
	seqIdx = 0
	for val in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == val:
			seqIdx += 1
	return seqIdx == len(sequence)
