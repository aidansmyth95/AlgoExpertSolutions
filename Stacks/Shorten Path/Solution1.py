'''
Relative path : name/
Absoloute path: /name/

Takes in valid Unix path. Condense it.
Split string by '/' - O(n) time for split functions
Filtering is also O(n) time
'''

# O(n) ST
def shortenPath(path):
	# relative or abs path?
    startsWithSlash = path[0] == "/"
	# filter out "/" characters that add no useful information post-split
	tokens = filter(isImportantToken, path.split("/"))
	stack = []
	if startsWithSlash:
		# re-add the empty string instead of forward slash. Call join later.
		stack.append("")
		
	# we can iter through tokens. When we see dir, add to stack. If we see
	# "..", pop values off stack - LIFO.
	for token in tokens:
		if token == "..":
			if len(stack) == 0 or stack[-1] == "..":
				# handle empty stack
				# keep track of consecutive double dots
				stack.append(token)
			elif stack[-1] != "":
				# can't ../ back from root. If not this case, pop stack.
				stack.pop()
		else:
			# append dir
			stack.append(token)
	
	if len(stack) == 1 and stack[0] == "":
		return "/"
	return "/".join(stack)
	
	
def isImportantToken(array):
	# filter out single full stops and empty strings
	return len(array) > 0 and array != "."
	
