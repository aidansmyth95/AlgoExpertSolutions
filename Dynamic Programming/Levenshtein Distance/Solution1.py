'''
Minimum number of edit ops to turn one string into another.
E.g.
	abc
	yabd
Answer: 2 (insert y, replace c with d)

Tough problem, dynamic programming problem.

E
	"" 	y	a	b	d
""	0	1	2	3	4
a	1	1	1	2	3
b	2	2	2	1	2
c	3	3	3	2	2* -> 2 is answer

If not sub-strings:
	We are checking 3 neighbouring boxes for minimum, and adding 1
	

Formula
__________
if str1[r-1] == str2[c-1]:
	E[r][c] = E[r-1][c-1] (diag up left)
else:
	E[r][c] = 1 + min(E[r-1][c-1], E[r-1][c], E[r][c-1])


'''

# O(NM) ST
def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	#print(edits)
	# set coulumns to be 0 - len(str2)
	for i in range(1, len(str2) + 1):
		edits[i][0] = edits[i - 1][0] + 1
	#print(edits)
	# now nested for loops...
	for r in range(1, len(str2) + 1):
		for c in range(1, len(str1) + 1):
			# and formula...
			if str2[r-1] == str1[c-1]:
				edits[r][c] = edits[r-1][c-1]
			else:
				edits[r][c] = 1 + min(
					edits[r-1][c-1],
					edits[r][c-1],
					edits[r-1][c])
	return edits[-1][-1]
