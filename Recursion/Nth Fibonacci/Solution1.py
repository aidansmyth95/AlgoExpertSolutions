# 0 1 1 2 3 5 8 13 21 ...
# here n=1 would return 0, n=2 would return 1 etc.
# ie there is no n=0 input
# Fn = F(n-1) + F(n-2). Let's use this as a recursive function


'''
# Naive way, time complexity isn't great
f6 -> f5 + f4 -> f4 + f3 + f3 + f2 -> and so on .....
So time is 2^n.
All fibNs are on call stack at one point, so O(n) S
'''

# O(2^n) T | O(n) S
def getNthFib(n):
	# recursive method
	if n ==1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-1) + getNthFib(n-2)
