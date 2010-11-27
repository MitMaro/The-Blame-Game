from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from models import Team, Point
from forms import AddPointForm
import service


def index(request):
	data = {
		'teams': Team.objects.filter(users__id=request.user.id)
	}
	return render_to_response('game/index.html', data, context_instance = RequestContext(request))
	
def score(request, team_id):
	points = service.getPointsForTeam(team_id)
	team = Team.objects.get(id=team_id)
	data = {
		'team': team,
		'points': points,
	}
	
	return render_to_response('game/score.html', data, context_instance = RequestContext(request))

def add(request, team_id):
	
	# default point object
	point = Point()
	point.team = Team.objects.get(id=team_id)
	
	# handle form
	if request.method == 'POST':
		add_form = AddPointForm(request.POST, instance=point)
		if add_form.is_valid():
			add_form.save()
			messages.success(request, "Point added.")
			return redirect('/game/score/' + str(team_id))
	else:
		add_form = AddPointForm(instance=point)
		
	data = {
		'team_id': team_id,
		'forms': {
			'add': add_form
		},
	}
	
	return render_to_response('game/add.html', data, context_instance = RequestContext(request))