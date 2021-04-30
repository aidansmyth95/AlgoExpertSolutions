'''
Find how many instances of x any y appear in our pattern.
Turn any pattern that starts with y into x, and record switch
'''

# O(n^2 + m) T - first 2 funcs run in O(m) and then O(n^2 for rest)
# O(n+m) S
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
		return []
	newPattern = getNewPattern(pattern)
	didSwitch = newPattern[0] != pattern[0]
	counts = {"x": 0, "y": 0}
	firstYPos = getCountsAndFirstYPosition(newPattern, counts)
	
	# if we have a y
	if counts["y"] > 0:
		# vary possible length of x
		for lenOfX in range(1, len(string)):
			lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
			if lenOfY <= 0 or lenOfY % 1 != 0:
				# invalid y, skip
				continue
			lenOfY = int(lenOfY) # ensure int
			# first y is after certain amount of Xs of lenOfX length
			yIdx = firstYPos * lenOfX
			x = string[:lenOfX]
			y = string[yIdx : yIdx + lenOfY]
			potMatch = map(lambda char: x if char == "x" else y, newPattern)
			if string == "".join(potMatch):
				# switch back x and y if didSwitch
				return [x, y] if not didSwitch else [y, x]
	else:
		lenOfX = len(string) / counts["x"]
		if lenOfX % 1 == 0:
			lenOfX = int(lenOfX)
			x = string[:lenOfX]
			potMatch = map(lambda char: x, newPattern)
			if string == "".join(potMatch):
				return [x, ""] if not didSwitch else ["", x]
	return []
			
def getNewPattern(array):
	pattern = list(array)
	if pattern[0] == "x":
		return pattern
	else:
		return list(map(lambda char: "x" if char == "y" else "y", pattern))
	
def getCountsAndFirstYPosition(pattern, counts):
	firstYPos = None
	for i, char in enumerate(pattern):
		counts[char] += 1
		if char == "y" and firstYPos is None:
			firstYPos = i
	return firstYPos