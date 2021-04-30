'''
When you win you get 3 points. Never a tie. 0 points for loss.
Competitions array - Strings define names of teams
our results order: awayTeam, homeTeam
'''
# O(n) T | O(k) S
# n is competitions and k is teams
def tournamentWinner(competitions, results):
    currentBestTeam = ""
	scores = {currentBestTeam: 0}
	
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition
		
		winningTeam = homeTeam if result == 1 else awayTeam
		updateScores(winningTeam, 3, scores)
		
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0
	scores[team] += points
