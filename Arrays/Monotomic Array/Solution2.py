'''
I like this clean solution
'''
# O(N) T | O(1) S
def isMonotonic(array):
	# assume both true at start
    isNonDecreasing = True
	isNonIncreasing = True
	# if both change, it is non-monotonic!
	for i in range(0, len(array)-1):
		if array[i+1] > array[i]:
			isNonIncreasing = False
		if array[i+1] < array[i]:
			isNonDecreasing = False
	return isNonIncreasing or isNonDecreasing