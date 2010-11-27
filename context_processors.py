from django.conf import settings as config

def settings(request):
	""" Give access to some of the application settings"""
	return {
		'DOMAIN': config.DOMAIN,
		'APPLICATION_TITLE': config.APPLICATION_TITLE,
		'COMPANY_NAME': config.COMPANY_NAME,
	}

def next(request):
	"""Make {{ NEXT }} available"""
	if 'next' in request.GET:
		return { 'NEXT': request.GET['next'] }
	elif 'next' in request.POST:
		return { 'NEXT': request.POST['next'] }
	else:
		return { 'NEXT': request.path }
