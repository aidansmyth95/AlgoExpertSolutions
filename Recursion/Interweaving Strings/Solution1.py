'''
Has very elegant recursive solution, that can be optimized a lot using caching.
If both letters at pointers equal next letter, explore both paths by recursion.

Solution 1 - no caching, brutal tie complexity. Tough to justify its complexity
Solution 2 becomes O(n*m)T, much better time complexity.
'''

# O(2^(n+m)) T | O(n+m) S
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
		return False
	
	return areInterwoven(one, two, three, 0, 0)

def areInterwoven(one, two, three, i, j):
	# k can be computed from i and j, no need to maintain
	k = i + j
	if k == len(three):
		return True
	
	# first case - when string 1 letter i is in string three, explore
	if i < len(one) and one[i] == three[k]:
		if areInterwoven(one, two, three, i + 1, j):
			return True

	# second case - when string 2 letter i is in string three, explore
	if j < len(two) and two[j] == three[k]:
		if areInterwoven(one, two, three, i, j + 1):
			return True
		
	return False
	