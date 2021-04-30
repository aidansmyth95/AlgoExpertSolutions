'''
We can shift elements backwards. 2 passes in changing direction.
'''
# O(n) T | O(1) S
def threeNumberSort(array, order):

	forwardIdx = 0
	backwardIdx = len(array) - 1
	
	# forward pass
	for i in range(len(array)):
		if array[i] == order[0]:
			# swap elements
			swap(array, i, forwardIdx)
			forwardIdx += 1
    
	# backward pass
	for j in range(len(array) - 1, forwardIdx - 1, -1):
		if array[j] == order[2]:
			# swap elements
			swap(array, j, backwardIdx)
			backwardIdx -= 1
	
	return array
	
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]