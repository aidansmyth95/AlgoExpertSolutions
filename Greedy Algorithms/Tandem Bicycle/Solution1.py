'''
Speed is max(a, b)
Sum total speeds of all pairs of riders at end
Greedy algorithm.
'''

# O(nlogn) T | O(1) S
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	
	if not fastest:
		# reverse red shirts
		reverseArrayInPlace(redShirtSpeeds)

	totalSpeed = 0
	
	for idx in range(len(redShirtSpeeds)):
		# move from left to right
		r1 = redShirtSpeeds[idx]
		# move from right to left
		b1 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
		totalSpeed += max(r1, b1)
		
	return totalSpeed

def reverseArrayInPlace(array):
	start = 0
	end = len(array) - 1
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1