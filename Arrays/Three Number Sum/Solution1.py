# Bad solutions:
# - 3 for loops / Hash table lookup

# O(N^2) T (two nested for loops) | #O(N) S (3N -> N)
def threeNumberSum(array, target_sum):
	triplets = []
    # sort array
	array.sort()
	# left and right pointer to try find answer
	for i in range(0, len(array) - 2):
		left_p = i + 1
		right_p = len(array) - 1
		while left_p < right_p:
			curr_sum = array[i] + array[left_p] + array[right_p]
			if curr_sum == target_sum:
				triplets.append([array[i], array[left_p], array[right_p]])
				left_p += 1
				
			elif curr_sum < target_sum:
				left_p += 1
			else:
				right_p -= 1
	return triplets