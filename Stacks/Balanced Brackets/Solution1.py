
# O(n) T | O(1) S
def balancedBrackets(string):
    '''
	We can pop from stack for closed and add to stack for opened
	'''
	openingBrackets = "([{"
	closingBrackets = ")]}"
	matchingBrackets = {")": "(", "]": "[", "}": "{"}
	stack = []
	for char in string:
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			if len(stack) == 0:
				return False
			elif stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	# make sure nothing left on stack at the end
	return len(stack) == 0
		