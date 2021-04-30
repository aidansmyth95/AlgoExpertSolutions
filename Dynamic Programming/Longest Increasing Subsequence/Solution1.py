'''
Dynamic programming

Lengths array - longest subseq up to index i
Sequences array - index of number that comes before it. Helps us build up answer

We can optimize this solution's time complexity further, using a binary search.
'''

# O(n^2) T | O(n) S
def longestIncreasingSubsequence(array):
    lengths = [1 for x in array]
	sequences = [None for x in array]
	maxLengthIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(i):
			otherNum = array[j]
			if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
				lengths[i] = lengths[j] + 1
				sequences[i] = j
		if lengths[i] >= lengths[maxLengthIdx]:
			maxLengthIdx = i
	return buildSequence(array, sequences, maxLengthIdx)
			
def buildSequence(array, sequences, idx):
	sequence = []
	while idx is not None:
		sequence.append(array[idx])
		idx = sequences[idx]
	return list(reversed(sequence))