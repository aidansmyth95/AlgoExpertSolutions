# O(n) time | O(n) space as we are adding n values to a hash table
def twoNumberSum(array, targetSum):
    # or we could do it in one for loop and a hash table
	# hash list nums that we will fill
	nums = {}
	ret = []

	for num in array:
		# what we would need to find to make pair
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			# if this is on hash table, we are done
			ret = [potentialMatch, num]
			break
		else:
			# store as True in hash table if found
			nums[num] = True
	return ret
