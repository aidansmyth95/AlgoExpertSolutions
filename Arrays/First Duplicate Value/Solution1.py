'''
I think we use hash table for this.
Check if we already have this value, if not add.

If we wanted O(1) S, we could use the O(N^2) T brute-force for loops code
'''

# dict
# O(N) T | O(N) S
def firstDuplicateValue(array):
    foundValues = {}
	for element in array:
		if element not in foundValues:
			foundValues[element] = True
		else:
			return element
    return -1

