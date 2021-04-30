'''
Sort in place: use just one extra copy of array (auxilliary array).
Main array is sorted in place using aux array.
'''

# O(nlogn) T | O(n) S
def mergeSort(array):
    if len(array) <= 1:
		return array
	auxArray = array[:]
	mergeSortHelper(array, 0, len(array) - 1, auxArray)
	return array

def mergeSortHelper(mainArray, startIdx, endIdx, auxArray):
	if startIdx == endIdx:
		return
	middleIdx = (startIdx + endIdx) // 2
	mergeSortHelper(auxArray, startIdx, middleIdx, mainArray)
	mergeSortHelper(auxArray, middleIdx + 1, endIdx, mainArray)
	doMerge(mainArray, startIdx, middleIdx, endIdx, auxArray)
	


def doMerge(mainArray, startIdx, middleIdx, endIdx, auxArray):
	k = startIdx
	i = startIdx
	j = middleIdx + 1
	
	while i <= middleIdx and j <= endIdx:
		if auxArray[i] < auxArray[j]:
			mainArray[k] = auxArray[i]
			i += 1
		else:
			mainArray[k] = auxArray[j]
			j += 1
		k += 1
	while i <= middleIdx:
		mainArray[k] = auxArray[i]
		i += 1
		k += 1
	while j <= endIdx:
		mainArray[k] = auxArray[j]
		j += 1
		k += 1