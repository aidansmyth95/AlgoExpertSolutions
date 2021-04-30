
# O(n) ST
def sunsetViews(buildings, direction):
    if direction == 'EAST':
		start_idx = len(buildings) - 1
		end_idx = - 1
		step = -1
	else:
		start_idx = 0
		end_idx = len(buildings)
		step = 1
		
	tallest = -1
	sunset = []
	for i in range(start_idx, end_idx, step):
		if buildings[i] > tallest:
			tallest = buildings[i]
			print(tallest)
			if direction == 'EAST':
				sunset.insert(0, i)
			else:
				sunset.append(i)
	return sunset