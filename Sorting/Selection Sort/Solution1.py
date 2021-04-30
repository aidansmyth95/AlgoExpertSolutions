'''
Go through from left pointer to end
Find min value
Swap with value at index left pointer
Increment left pointer

While and for loop so O(N^2) time

Not the best performance sorting algorithm
'''

# Average:  O(N^2) Time | O(1) Space
# Best: O(N^2) Time | O(1) Space
# Worst:  O(N^2) Time | O(1) Space
def selectionSort(array):
    left_idx = 0
	while left_idx < len(array) - 1:
		min_idx = left_idx
		# find and update min value
		for i in range(left_idx, len(array)):
			if array[i] < array[min_idx]:
				min_idx = i
		# swap with left pointer
		swap(array, left_idx, min_idx)
		# inrement left_idx
		left_idx += 1
	return array

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
