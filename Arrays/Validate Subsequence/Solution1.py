# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	# only look for one lement at a time in subsequence
	# traverse, find all of them
	# check length of those found
	arrIdx = 0
	seqIdx = 0
	# increment pointer in seqIdx once it is found
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)
