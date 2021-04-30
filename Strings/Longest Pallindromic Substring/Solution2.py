'''
Solution 2
Iterate through a string. For each point, treat it as if it could be the
centre of a palindrome.
Can be of odd or even length, this affect centre of palindrome.
'''
# O(n^2)  | O(n) S
def longestPalindromicSubstring(string):
    # slicing indeces of longest - starting and (ending index + 1) of palindrome
	currentLongest = [0, 1]
	for i in range(1, len(string)):
		# palindrom of odd length centred at letter - left_idx and right_idx
		odd = getLongestPalindromeFrom(string, i - 1, i + 1)
		even = getLongestPalindromeFrom(string, i - 1, i)
		# judges which is longest by taking difference of two array values
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
	return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	# current leftIdx is one too far to the left.
	# rightIdx needs to be +1 since we are slicing in this implementation
	return [leftIdx + 1, rightIdx]
			


