'''
Iterative one to reduce space usage
We store array to have last 2 fib numbers
This is the best
'''

# O(N) T | O(1) S
def getNthFib(n):
    # Write your code here.
    array = [0, 1]
	counter = 3 # since we have 2 already, time to calculate 3
	# our fN function
	while counter <= n:
		# calculate next Fib number from array
		fibN = array[0] + array[1]
		# update array
		array = [array[1], fibN]
		counter += 1
	# if n=1, return 0 which would have been array[0]
	return array[1] if n > 1 else array[0]