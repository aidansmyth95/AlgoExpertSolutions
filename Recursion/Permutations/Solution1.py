def getPermutations(array):
    permutations = []
	getPermutationsHelper(array, [], permutations)
	return permutations


# O(n! * n^2) T | O(n! * n) S
def getPermutationsHelper(array, currentPerm, permutations):
	'''
	Go from left to right through array.
	'''
	
	# if array is empty, append currentPerm to permutations
	# else, for each number make it the first in the next perm
	
	if not len(array) and len(currentPerm):
		permutations.append(currentPerm)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i+1:]
			print(newArray)
			newPerm = currentPerm + [array[i]]
			getPermutationsHelper(newArray, newPerm, permutations)