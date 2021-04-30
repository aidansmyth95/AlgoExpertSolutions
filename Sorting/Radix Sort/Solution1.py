'''
Array of positive integers.
Sort using radix sort algo.
When we know nothing about our input, O(nlogn) is best we can do.
If we know info about our input data, we can often sort faster than O(nlogn)
Example: counting sort
Radix sort sorts by significant digits, one digit at a time.
We know all are positive and digits are in range 1-b. Called d times, where d
is number of digits in max number.
'''

# O(d * (n + b)) T | O(n+b) S
def radixSort(array):
    if len(array) == 0:
		return array
	
	maxNumber = max(array)
	digit = 0
	while maxNumber / 10 ** digit > 0:
		countingSort(array, digit)
		digit += 1
	return array

def countingSort(array, digit):
	sortedArray = [0] * len(array)
	countArray = [0] * 10
	digitCol = 10 ** digit
	
	for num in array:
		countIdx = (num // digitCol) % 10
		countArray[countIdx] += 1
		
	for idx in range(1, 10):
		countArray[idx] += countArray[idx - 1]
		
	for idx in range(len(array) - 1, -1, -1):
		countIdx = (array[idx] // digitCol) % 10
		countArray[countIdx] -= 1
		sortedIdx = countArray[countIdx]
		sortedArray[sortedIdx] = array[idx]
		
	for idx in range(len(array)):
		array[idx] = sortedArray[idx]
