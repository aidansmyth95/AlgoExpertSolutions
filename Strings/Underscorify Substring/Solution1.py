'''
When substring overlaps with itself, only do at its extremeties.
1. Find idx of every location of substring - getLocations
2. Only keep far end underscores - collapseLocations
3. Add underscores to string - underscorify

'''

# O(n + m) - getLocations .find runs in O(n+m) after amoritization
# O(n) S
def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
	return underscorify(string, locations)

def getLocations(string, substring):
	locations = []
	startIdx = 0
	while startIdx < len(string):
		nextIdx = string.find(substring, startIdx)
		# check if present
		if nextIdx != -1:
			locations.append([nextIdx, nextIdx + len(substring)])
			startIdx = nextIdx + 1
		else:
			# if not present
			break
	return locations

def collapse(locations):
	# collapsing two arrays: [a b], [c d] -> [a d]
	if not len(locations):
		return locations
	newLocations = [locations[0]]
	previous = newLocations[0]
	for i in range(1, len(locations)):
		# for each 2-element list [c d]
		current = locations[i]
		# if c <= b -> collapse
		if current[0] <= previous[1]:
			# b = d
			previous[1] = current[1]
		else:
			newLocations.append(current)
			previous = current
	return newLocations

def underscorify(string, locations):
	locationsIdx = 0
	stringIdx = 0
	inBetweenUnderscores = False
	finalChars = []
	i = 0
	while stringIdx < len(string) and locationsIdx < len(locations):
		if stringIdx == locations[locationsIdx][i]:
			# we put underscore
			finalChars.append("_")
			# flip flag
			inBetweenUnderscores = not inBetweenUnderscores
			# if we are not in between underscores, we want to move in
			# locations array
			if not inBetweenUnderscores:
				locationsIdx += 1
			i = 0 if i == 1 else 1 # toggle i position in locations
		# regardless, append string
		finalChars.append(string[stringIdx])
		stringIdx += 1
	# if there is a _ left to append, append at end
	if locationsIdx < len(locations):
		finalChars.append("_")
	elif stringIdx < len(string):
		# if we are not done with string
		finalChars.append(string[stringIdx:])
	return "".join(finalChars)