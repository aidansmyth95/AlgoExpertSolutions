'''
A divide and conquer algorithm.
Second solution is better from space complexity and sorts in place.
At lowest level we merge two subarrays of len 2, checking their order once sorted


'''

# O(nlogn) ST ... ALWAYS!
def mergeSort(array):
    if len(array) == 1:
		return array
	middleIdx = len(array) // 2
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	return mergeSortArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortArrays(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0
	while i< len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		k += 1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	return sortedArray