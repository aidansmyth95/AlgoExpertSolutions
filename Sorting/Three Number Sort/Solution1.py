'''
Small array only ever has 3 elements
Modified bucket sort.
Create m buckets that keep count of their elements.
Downside is multiple iterations of array (2-4 times)...
'''

# O(n) T | O(1) S
def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]
	for element in array:
		# get index in smaller array
		orderIdx = order.index(element)
		valueCounts[orderIdx] += 1
		
	for i in range(3):
		value = order[i]
		count = valueCounts[i]
		numElementsBefore = sum(valueCounts[:i])
		for n in range(count):
			currentIdx = numElementsBefore + n
			array[currentIdx] = value
			
	return array
