def getPermutations(array):
    permutations = []
	getPermutationsHelper(array, 0, permutations)
	return permutations

# O(n * n!) ST
def getPermutationsHelper(array, i, permutations):
	'''
	Keep swapping elements to and from, building permutation
	Difference to solution 1 is that swaps are O(1)...
	'''
	
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i, j)
			getPermutationsHelper(array, i + 1, permutations)
			swap(array, i, j)
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]