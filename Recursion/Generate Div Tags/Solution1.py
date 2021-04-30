'''
Number of html div tags output must contain
Open + Close = 1 tag
For every opening, ther emust be a closed
1: open close
2: open open close close, open close open close
3: more options and so on...
If you keep going, you get exponentially increasing number of tags. Not easy
by any means.

Recursively generate all possible strings
'''

# O((2n)! / (n!((n+1)!))) ST - never will have to come up with this! :)
def generateDivTags(numberOfTags):
    matchedDivTags = []
	generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchedDivTags)
	return matchedDivTags

def generateDivTagsFromPrefix(openingTags, closingTags, prefix, result):
	# if we require any, it is always valid to add one
	if openingTags > 0:
		newPrefix = prefix + "<div>"
		generateDivTagsFromPrefix(openingTags - 1, closingTags, newPrefix, result)

	# if we still need to add a closing tag, we can add one
	if openingTags < closingTags:
		newPrefix = prefix + "</div>"
		generateDivTagsFromPrefix(openingTags, closingTags - 1, newPrefix, result)

	# we have completed a string, add it to result
	if closingTags == 0:
		result.append(prefix)
