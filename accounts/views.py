from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from forms import LoginForm, RegisterForm, AccountForm
import TheBlameGame.service
import service as service
from django.contrib.auth.decorators import login_required


def login(request):
	# user is already logged in
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
		
	# get the referral
	referral = TheBlameGame.service.getSecureReferral(request)
	
	# handle form
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			if service.login(
				request,
				login_form.cleaned_data['username'],
				login_form.cleaned_data['password']
			):
				messages.success(request, 'You have been logged in')
				return HttpResponseRedirect(referral)
			else:
				messages.error(request, 'Username and password did not match')
	else:
		login_form = LoginForm()
		
	data = {
		'forms': {
			'login': login_form
		},
	}
	
	return render_to_response('accounts/login.html', data, context_instance = RequestContext(request))
	

def register(request):
	# user is already logged in
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			user = service.register(
				register_form.cleaned_data['username'],
				register_form.cleaned_data['firstname'],
				register_form.cleaned_data['lastname'],
				register_form.cleaned_data['email'],
				register_form.cleaned_data['password'],
			)
			messages.success(
				request,
				'You have successfully been signed up.'
			)
			user = service.login(request, register_form.cleaned_data['username'], register_form.cleaned_data['password'])
			if not user:
				messages.error(
					request,
					'There was a problem loging you in. Please login using your credientials'
				)
				
			return HttpResponseRedirect('/')
	else:
		register_form = RegisterForm()
		
		
	data = {
		'forms': {
			'register': register_form
		},
	}
	return render_to_response('accounts/register.html', data, context_instance = RequestContext(request))

def logout(request):
	messages.success(request, 'You have been logged out')
	service.logout(request)
	return HttpResponseRedirect('/')

@login_required
def account(request):
	if request.method == 'POST':
		account_form = AccountForm(request.POST)
		if account_form.is_valid():
			user = service.update(
				request.user,
				account_form.cleaned_data['first_name'],
				account_form.cleaned_data['last_name'],
				account_form.cleaned_data['password'],
			)
			messages.success(
				request,
				'Your account has successfully been updated.'
			)
	else:
		account_form = AccountForm(instance=request.user)
		
	data = {
		'forms': {
			'account': account_form
		},
	}
	return render_to_response('accounts/account.html', data, context_instance = RequestContext(request))

