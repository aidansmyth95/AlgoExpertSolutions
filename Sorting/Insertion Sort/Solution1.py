'''
Left most element is considered sorted. Then for each
element to the right, keep checking left where it needs to be inserted.
Then insert
'''

# Avg O(N^2) Time | O(1) space
# Best O(N) Time | O(1) space
# Worst O(N^2) Time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
		# start at new left index 'j' each time
		j = i
		# compare j and j-1
		while j > 0 and array[j] < array[j - 1]:
			# swap as many as we can for j until no more swap needed
			swap(array, j, j - 1)
			j -= 1
	return array

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]