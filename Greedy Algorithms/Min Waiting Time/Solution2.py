
# Sub-optimal first attempt
# O(n^2)T | O(1) S
def minimumWaitingTime(queries):
    # minimum waiting time
	# only positive integers in array

	# step 1 - find new order for queries
	# step 2 - running sum n times o f n elements

	qTime = 0
	if len(queries) == 1:
		# immediate for only one query
		return qTime
	
	# we want largest queries to be run last
	# lets sort array to be ascending
	queries.sort()
	for i in range(0, len(queries)):
		qTime += sum(queries[:i])
	return qTime
