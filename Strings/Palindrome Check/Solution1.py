#! Two solutions in this file

'''
Copy & reverse string and check if same
For loop and a copy each time (string is immutable in Python), so O(N^2) T
Copy is O(N) space
'''

# O(N^2) T and O(N) space
def isPalindrome(string):
    reversed_string = ""
	# create reversed string
	for i in range(len(string)-1, -1, -1):
		reversed_string += string[i]
	#print('{} {}'.format(reversed_string, string))
	return reversed_string == string

'''
Instead of creating a new string, store everything in one array
and compare at end
'''
# O(N) Time | O(N) Space
def isPalindrome(string):
    reversed_string = []
	# create reversed string
	for i in range(len(string)-1, -1, -1):
		reversed_string.append(string[i])
	reversed_string = "".join(reversed_string)
	#print('{} {}'.format(reversed_string, string))
	return reversed_string == string