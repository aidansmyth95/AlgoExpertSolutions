'''
Has very elegant recursive solution, that can be optimized a lot using caching.
If both letters at pointers equal next letter, explore both paths by recursion.

Solution 1 - no caching, brutal tie complexity
Solution 2 becomes O(n*m)T, much better time complexity.

We use caching
'''

# O(n*m) T | O(n*m) S
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
		return False
	
	cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
	return areInterwoven(one, two, three, 0, 0, cache)

def areInterwoven(one, two, three, i, j, cache):
	
	# check cache first, return if not None
	if cache[i][j] is not None:
		return cache[i][j]
	
	# k can be computed from i and j, no need to maintain
	k = i + j
	if k == len(three):
		return True
	
	# first case - when string 1 letter i is in string three, explore
	if i < len(one) and one[i] == three[k]:
		cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
		if cache[i][j]:
			return cache[i][j]

	# second case - when string 2 letter i is in string three, explore
	if j < len(two) and two[j] == three[k]:
		cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
		if cache[i][j]:
			return cache[i][j]
	
	# no interwoven string
	cache[i][j] = False
	return False
	