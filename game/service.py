from django.contrib.auth.models import User
from game.models import Point, Team

def addPoint(blame_username, fixer_username):
	blame = User.objects.get(username=blame_username)
	fixer = User.objects.get(username=fixer_username)
	point = Point()
	point.blame = blame
	point.fixer = fixer
	point.save()
	return point

def getPointsForTeam(team_id):
	points = Point.objects.filter(team__id__exact = team_id)
	players = User.objects.filter(team__id__exact = team_id)
	
	rtn = {
		'total': len(points),
		'players': {}
	}
	
	# build basic data structure
	for player in players:
		rtn['players'][player.username] = {
			'total_fixes': 0,
			'total_breaks': 0,
			'player': player,
			'fixes': {}
		}
		for other_player in players:
			rtn['players'][player.username]['fixes'][other_player.username] = 0
			
	# loop over points adding to the above data structure
	for point in points:
		rtn['players'][point.fixer.username]['total_fixes'] += 1
		rtn['players'][point.blame.username]['total_breaks'] += 1
		rtn['players'][point.fixer.username]['fixes'][point.blame.username] += 1
		
	return rtn