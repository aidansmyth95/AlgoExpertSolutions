'''
Could we use recursion?

Is the first letter == last letter, keep making string smaller...
O(N/2) calls -> O(N) ST

'''
# O(N) Time | O(N/2) = O(N) Space
# Tail recursion might give us O(1) Space depending on the compiler,
# but it might not...
def isPalindrome(string, i=0):
	# upper index to check is j, lower limit is i
	j = len(string) - 1 - i
	# Tail recursion attempt - depends on compiler, miiiight make O(1)
	if i >= j:
		return True
	elif string[i] != string[j]:
		return False
	return   isPalindrome(string, i + 1)