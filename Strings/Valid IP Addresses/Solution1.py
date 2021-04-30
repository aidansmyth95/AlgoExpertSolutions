'''
Invalid if leading 0 followed by integer, e.g. 01 or 02...
Also, integer must be <= 255
3 full stops to be inserted
Length must be <= 4 positive integers
'''

# O(1) T | O(1) S - this solution does ot depend on the size of the input!
# 8 bits * 4 sections = 32 bits.
# it is at most size of 12! So at most, 2^32 IP addresses to generate.
# So O(2^32), a constant upper bound. So O(1).
def validIPAddresses(string):
    addressesFound = []
	
	# first section combos
	for i in range(1, min(len(string), 4)):
		currentAddressParts = ["", "", "", ""]
		currentAddressParts[0] = string[:i]
		if not isValidPart(currentAddressParts[0]):
			continue
		
		# second section combos
		for j in range(i + 1, i + min(len(string) - i, 4)):
			currentAddressParts[1] = string[i:j]
			if not isValidPart(currentAddressParts[1]):
				continue
			
			# third section combos
			for k in range(j + 1, j + min(len(string) - j, 4)):
				currentAddressParts[2] = string[j:k]
				currentAddressParts[3] = string[k:]
				if isValidPart(currentAddressParts[2]) and isValidPart(currentAddressParts[3]):
					# join with periods
					addressesFound.append(".".join(currentAddressParts))

	return addressesFound
			
def isValidPart(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	# check for leading zero
	return len(string) == len(str(stringAsInt))
	
	
