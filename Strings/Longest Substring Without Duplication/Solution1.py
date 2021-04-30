
# O(n) T
# O(min(n, m)) S
def longestSubstringWithoutDuplication(string):
    longest = [0, 1]
	lastSeen = {}
	startIdx = 0
	for i, char in enumerate(string):
		if char in lastSeen:
			# how long have we gone since we have seen it before
			startIdx = max(startIdx, lastSeen[char] + 1)
		if longest[1] - longest[0] < i + 1 - startIdx:
			longest = [startIdx, i + 1]
		lastSeen[char] = i
	return string[longest[0] : longest[1]]
			
