
# Optimal second attempt
# O(nlog(n))T | O(1) S
def minimumWaitingTime(queries):
    # minimum waiting time
	# only positive integers in array

	# step 1 - find new order for queries
	# step 2 - add value*elements_left in for loop

	qTime = 0
	qLeft = len(queries)
	if qLeft == 1:
		# immediate for only one query
		return qTime
	
	# we want largest queries to be run last
	# lets sort array to be ascending
	queries.sort()
	for i, value in enumerate(queries):
		qLeft -= 1
		qTime += qLeft * value
	return qTime


