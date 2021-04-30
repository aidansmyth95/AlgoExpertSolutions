# O(n * 2^n) ST - we double n time our subsets
def powerset(array, idx=None):
	subsets = [[]]
	for ele in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [ele])
	return subsets