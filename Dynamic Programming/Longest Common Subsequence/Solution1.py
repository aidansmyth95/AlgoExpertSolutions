'''
A set of characters obtained by removingsome characters from string and
maintaining order.
LCS = longest common substring.
We will use Dynamic programming, by building 2D array.
"" serve as a base case.
We compare last two letters.
	If not equal we take longest LCS above it or to left the left of it.
	If equal, we append to diagonally located LCS
	If we can pic e.g. X or Z, pick one arbitrarily


	""	X	K	Y	K	Z	P	W
""	""	""	""	""	""	""	""	""
Z	""	""	""	"" 	""	Z	Z	Z
X	""	X	X	X	X	X	X	X
V	""	X	X	X	X	X	X	X
V	""	X	x	x	x	x	X	X
Y	""	X	X	XY	XY	XY	XY	XY
Z	""	X	X	XY	XY	XYZ	XYZ	XYZ
W	""	X	X	XY	XY	XYZ	XYZ	XYZW -> answer

Strings n and m length
When we have a LCS, we are adding, e.g. XYZ + W = XYZW
Longest LCS you can have is min(n,m), and this would be time to concat to
the string
O(n*m*min(n,m))
We could improve space complexity by only looking at two rows.
We could also not store the LCS and concat them. Instead we could just store
pointers and booleans.
'''

# O(n*m*min(n,m)) ST
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
	for i in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if str2[i-1] == str1[j-1]:
				lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)

	return lcs[-1][-1]
