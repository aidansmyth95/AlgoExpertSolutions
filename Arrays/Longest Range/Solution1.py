'''
Build a hash table and then heck it for longest range
'''
# O(n) ST
def largestRange(array):
	bestRange = []
	longestLength = 0
	# build hash map of numbers
	nums = {}
	for num in array:
		nums[num] = True
	
	# iterate through hash map, building up longest length and range
	for num in array:
		if not nums[num]:
			continue
		nums[num] = False
		currentLength = 1
		left = num - 1
		right = num + 1
		# update count of consecutive numbers to left and right of it found
		while left in nums:
			nums[left] = False
			currentLength += 1
			left -= 1
		while right in nums:
			nums[right] = False
			currentLength += 1
			right += 1
		# at end, check if length > longest, and if so update range
		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left + 1, right - 1]
	return bestRange