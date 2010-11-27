from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from accounts.forms import LoginForm, RegisterForm

def index(request):
	
	# user is already logged in
	if request.user.is_authenticated():
		return redirect('game-index')
	
	data = {
		'forms': {
			'register': RegisterForm(),
			'login': LoginForm()
		}
	}
	
	return render_to_response('default/index.html', data, context_instance = RequestContext(request))
