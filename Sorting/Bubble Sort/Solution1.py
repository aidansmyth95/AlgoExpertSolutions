'''
My understanding. We pass N times, each time we go a little less...
Stop at 0, stop at 1, stop at 2...

Bubble sort swaps elements one by one as we reverse traverse an array
We can traverse a little less each time
'''

# Average O(N^2) time | O(1) space
# Best O(N) time
# Worst = average
def bubbleSort(array):
    right_idx = len(array) - 1
	left_idx = 0
	
	while left_idx < right_idx:
		for i in range(right_idx, left_idx, -1):
			# check values at i and i-1, swap if necessary
			if array[i-1] > array[i]:
				swapPair(array, i-1, i)
		left_idx += 1
	return array

def swapPair(array, a_idx, b_idx):
	# swap
	tmp = array[b_idx]
	array[b_idx] = array[a_idx]
	array[a_idx] = tmp
