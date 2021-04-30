'''
We can use dynamic programming
Create array of same length. At each index, have value of greatest subseq
that can be built up to and including that index in the array
'''

# O(n^2) T | O(n) S
def maxSumIncreasingSubsequence(array):
	# we store index of previous subsequence tat ends at that index
	sequences = [None for _ in array]
	# we also store sums so we can max sum
	sums = [num for num in array]
	maxSumIdx = 0
	# for loop to fill each elements of sequences and sums
	for i in range(len(array)):
		currentNum = array[i]
		# for loop on previous elements to see what values < currentNum
		for j in range(0, i):
			otherNum = array[j]
			# if less than, and its sums value with current value is a new max
			# sum for that idx, update results at that idx for now
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequences[i] = j
		# update overall max sums and seq
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
	return [sums[maxSumIdx], buildSequences(array, sequences, maxSumIdx)]
	
def buildSequences(array, sequences, idx):
	sequence = []
	while idx is not None:
		# move backwards, appending
		sequence.append(array[idx])
		idx = sequences[idx]
	# reverse and return to be in correct order of appearance in array
	return list(reversed(sequence))
		
