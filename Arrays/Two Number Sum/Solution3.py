# O(nlogn) time | O(1) space
# sort array nlogn time, and we find in O(n) time, so O(nlogn)
def twoNumberSum(array, targetSum):
	array.sort()
	res = []
	# sum extremes, compare to number
	# if < than, move left pointer to the right
	# otherwise move right pointer to the left
	# idx pointer values
	l_p = 0
	r_p = len(array) - 1
	while l_p < r_p:
		resSum = array[l_p] + array[r_p]
		if resSum == targetSum:
			res = [array[l_p], array[r_p]]
			return res
		elif resSum < targetSum:
			l_p += 1
		elif resSum > targetSum:
			r_p -= 1
	return res