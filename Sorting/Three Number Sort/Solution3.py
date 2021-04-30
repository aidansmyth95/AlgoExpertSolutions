'''
We can do in 1 pass. Same as previous decision, but all at once.
Look with secondIdx pointer, swap with first or second and move all pointers.
'''
# O(n) T | O(1) S
def threeNumberSort(array, order):

	# where we should insert elements in our ordering
	firstIdx = 0
	secondIdx = 0
	thirdIdx = len(array) - 1
	
	# single pass
	while secondIdx <= thirdIdx:
		if array[secondIdx] == order[0]:
			# swap with first, increment first
			swap(array, firstIdx, secondIdx)
			firstIdx += 1
			# increment second
			secondIdx += 1
		elif array[secondIdx] == order[2]:
			# swap with third, decr. third
			swap(array, thirdIdx, secondIdx)
			thirdIdx -= 1
		else:
			# increment second
			secondIdx += 1

	return array
	
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]