'''
Two for loops approach the best one?
'''

# O(N^2) T | O(N) S
def arrayOfProducts(array):
    result = []
	for i in range(len(array)):
		# now product the others
		val = 1
		for j in range(len(array)):
			if i != j:
				val *= array[j]
		result.append(val)
		
	return result
