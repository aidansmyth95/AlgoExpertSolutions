'''
How about we save the values so we can lookup fN values
and not recall needlessly? This saves us time, we can use
lots of constant time lookups instead and only N function calls.
'''

# O(N) T | O(N) S
def getNthFib(n, memorize = {1: 0, 2: 1}):
	# memorize will be a hash table.
	# we can add n = {1,2} to it.
	# It needs to be passable as an input param

	# recursive method
	if n in memorize:
		return memorize[n]
	else:
		memorize[n] = getNthFib(n-1, memorize) + getNthFib(n-2, memorize)

	return memorize[n]
