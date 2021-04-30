
# O(n * 2^n) ST - we double n time our subsets
def powerset(array, idx=None):
    if idx is None:
		idx = len(array) - 1
	if idx < 0:
		return [[]]
	ele = array[idx]
	subsets = powerset(array, idx - 1)
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset + [ele])
	return subsets
