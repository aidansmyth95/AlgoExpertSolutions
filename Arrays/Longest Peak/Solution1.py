'''
Peak: numbers either side are lower. Peak is until a side changes again.
Peak is the index, not related to actual array value magnitude!

For until we see a negative change between i and i+1 -> might be a peak
Follow the negative chnage until it becomes positive again.
Difference between peak idx and lowest idx is length of peak.
'''

# O(N) T | O(1) S
def longestPeak(array):
	longestPeakLength = 0
	i = 1
	while i < len(array) - 1:
		# check if each element is a peak
		isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
		if not isPeak:
			i += 1
			continue
		
		# we have a peak. Now determine how many elements long
		left_idx = i - 2
		while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
			left_idx -= 1
		right_idx = i + 2
		while right_idx <= len(array) - 1 and array[right_idx] < array[right_idx - 1]:
			right_idx += 1
			
		currPeakLength = right_idx - left_idx - 1
		longestPeakLength = max(longestPeakLength, currPeakLength)
		i = right_idx
		
	return longestPeakLength