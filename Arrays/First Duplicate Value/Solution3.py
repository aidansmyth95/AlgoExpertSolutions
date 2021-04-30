'''
This is REALLY smart.
# we can mutate array in O(1) time.
Idea -> since between 1 and N, mutate value of array at i-1
'''

# O(N) T | O(1) S -> array mutation is O(1) S, no external data struct
def firstDuplicateValue(array):
	for element in array:
		copied_element = abs(element)
		# if value is already negative, we have seen this before
		if array[copied_element - 1] < 0:
			return copied_element
		# make it negative
		array[copied_element - 1] *= -1
	return -1