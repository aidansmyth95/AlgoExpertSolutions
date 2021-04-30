'''
We can use unicode values instead of a hash table
ord() does this in Python
	a -> 97
	z -> 122
	
O(N) T as a for loop for N characters and single char const time ops
O(N) S as creating a new string size N
'''

# O(N) ST
# However, if alphabet was Big and size M, alphabet lookup would be O(M)T
def caesarCipherEncryptor(string, key):
	new_string = []
	
	# list for going from int back to char
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	# use a as 0 idx
	ord_a = ord('a')

	# handle if key > 26 with modulo
	newKey = key % 26

	# for every string character, find integer (0-25 inc), add 2, modulo, and get char again
	for i in range(len(string)):
		# add value to string and modulo num letters
		old_integer_val = ord(string[i]) - ord_a
		new_integer_idx = (old_integer_val + newKey) % 26
		new_string.append(alphabet[new_integer_idx])
	new_string = "".join(new_string)
	return new_string
