# O(N) time | O(1) space (we are not using any other data struct, doing in place)
def moveElementToEnd(array, toMove):
    left_p = 0
	right_p = len(array) - 1
	# while two pointers don't overlap
	while (left_p < right_p):
		# do a swap
		if array[left_p] == toMove and array[right_p] != toMove:
			array[left_p], array[right_p] = array[right_p], array[left_p]
		# move right pointer until it is at value that is not toMove
		if array[right_p] == toMove:
			right_p -= 1
		# move left pointer unil it is at value toMove
		if array[left_p] != toMove:
			left_p += 1
	return array
