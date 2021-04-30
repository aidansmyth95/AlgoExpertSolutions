# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

'''
Special array
- non-empty
- contains either integers or other special arrays
- product sum of it is the sum of its elements, where special
	arrays inside it are called and multipled by their depth level
- depth is how nested it is. First [] is depth 1, inner of [[]] is depth 2 etc
- [x,y] = x+y
- [x, [y,z]] = x + 2(y+z)

'''

# O(N) time | O(d) space where d is greatest depth
def productSum(array, depth=1):
    prodSum = 0
	for element in array:
		if type(element) is list:
			# recursive call
			prodSum += productSum(element, depth + 1)
		elif type(element) is int:
			prodSum += element
		else:
			print("OOPS!")
    return prodSum * depth
