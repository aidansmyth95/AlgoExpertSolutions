# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    ret = []
	for i, element_a in enumerate(array):
		for j, element_b in enumerate(array):
			if i != j and element_a + element_b == targetSum:
				# if not same array idx and meet criteria
				ret = [element_a, element_b]
				return ret
	return ret
				