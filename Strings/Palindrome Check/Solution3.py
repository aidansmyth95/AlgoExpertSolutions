'''
Iterative optimal solution

We can't do better than O(N) T, but we can do better with space.
Yes, we can go from O(N) space to O(1) space if we use iterative approach.
While loop, check and move pointers until they overlap
'''

# O(N)T | O(1)S
def isPalindrome(string, i=0):
	left_idx = 0
	right_idx = len(string) -1
	
	while left_idx < right_idx:
		# check to see if False
		if string[left_idx] != string[right_idx]:
			return False
		left_idx +=1
		right_idx -= 1
	return True