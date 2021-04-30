'''
Both ppl need to not have meetings in calendars in that range, and that
range needs to be >= target meeting length.
We can create two additional meetings at bounds of work day to show busy
Then merge the calendars to find availabilities of both individuls, do this
in a merge sort kind of way.
Then we can merge/flatten overapping meetings into one.
Then chack all the gaps: ending of previous to start of current
'''

# O(c1 + c2) T | O(c1 + c2) S
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # update to include daily bounds as busy meetings
	updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
	mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
	flattenedCalendar = flattenCalendar(mergedCalendar)
	return getMatchingAvailabilities(flattenedCalendar, meetingDuration)
	
def updateCalendar(calendar, dailyBounds):
	# make copy of original calendar
	updatedCalendar = calendar[:]
	updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
	updatedCalendar.append([dailyBounds[1], "23:59"])
	return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))

def timeToMinutes(time):
	hours, mins = list(map(int, time.split(":")))
	return hours * 60 + mins

def minutesToTime(minutes):
	hours = minutes // 60
	mins = minutes % 60
	hoursString = str(hours)
	minutesString = "0" + str(mins) if mins < 10 else str(mins)
	return hoursString + ":" + minutesString
	
def mergeCalendars(calendar1, calendar2):
	merged = []
	i, j = 0, 0
	while i < len(calendar1) and j < len(calendar2):
		meeting1, meeting2 = calendar1[i], calendar2[j]
		if meeting1[0] < meeting2[0]:
			merged.append(meeting1)
			i += 1
		else:
			merged.append(meeting2)
			j += 1
	# handle left overs at end
	while i < len(calendar1):
		merged.append(meeting1)
		i += 1
	while j < len(calendar2):
		merged.append(meeting2)
		j += 1
	return merged
		

def flattenCalendar(calendar):
	# copy calendar to be safe
	flattened = [calendar[0][:]]
	for i in range(1, len(calendar)):
		currMeeting = calendar[i]
		# can last flattened array item be extended?
		prevMeeting = flattened[-1]
		currStart, currEnd = currMeeting
		prevStart, prevEnd = prevMeeting
		if prevEnd >= currStart:
			# new merged meeting block duration
			newPrevMeeting = [prevStart, max(prevEnd, currEnd)]
			flattened[-1] = newPrevMeeting
		else:
			# we had two detached meetings - append a copy
			flattened.append(currMeeting[:])
	return flattened

def getMatchingAvailabilities(calendar, meetingDuration):
	matchingAvail = []
	for i in range(1, len(calendar)):
		start = calendar[i - 1][1]
		end = calendar[i][0]
		duration = end - start
		if duration >= meetingDuration:
			matchingAvail.append([start, end])
	# stringify
	return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvail))