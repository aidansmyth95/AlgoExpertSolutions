'''
arr[a] - arr[b] + arr[c] - arr[d], where a < b < c < d
Brute force is O(n^4), we can do better.
'''

# O(n) ST
def maximizeExpression(array):
    if len(array) < 4:
		return 0
	
	maxOfA = [array[0]]
	maxOfAMinusB = [float("-inf")]
	maxOfAMinusBPlusC = [float("-inf")] * 2
	maxOfAMinusBPlusCMinusD = [float("-inf")] * 3
	
	for idx in range(1, len(array)):
		currentMax = max(maxOfA[idx - 1], array[idx])
		maxOfA.append(currentMax)

	for idx in range(1, len(array)):
		currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
		maxOfAMinusB.append(currentMax)

	for idx in range(2, len(array)):
		currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
		maxOfAMinusBPlusC.append(currentMax)

	for idx in range(3, len(array)):
		currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
		maxOfAMinusBPlusCMinusD.append(currentMax)

	return maxOfAMinusBPlusCMinusD[-1]