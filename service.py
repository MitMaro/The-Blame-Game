from django.conf import settings

def getSecureReferral(request):
	""" Return a secure request referral that does not allow referrals outside the application""" 
	# try to get referral from next in request or from the referer
	if 'next' in request.GET:
		referral = request.GET['next']
	elif 'next' in request.POST:
		referral = request.POST['next']
	else:
		referral = request.META.get('HTTP_REFERER', False) or '/'
	
	# safe url
	if (referral.startswith(settings.DOMAIN) or
		referral.startswith('http://' + settings.DOMAIN) or
		referral.startswith('https://' + settings.DOMAIN)):
		return referral
	
	# no absolute urls (at least not from this domain)
	if (referral.startswith('http:') or
		referral.startswith('https:') or
		referral.startswith('ftp:')):
		referral = '/'
	# all other referrals add a slash to make it an absolute path
	elif not referral.startswith('/'):
		print "here"
		referral = '/' + referral
	return referral
