# Set
# O(N) T | O(N) S
def firstDuplicateValue(array):
    foundValues = set()
	for element in array:
		if element not in foundValues:
			foundValues.add(element)
		else:
			return element
    return -1