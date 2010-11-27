from django.contrib import auth
from django.contrib.auth.models import User

def login(request, username, password):
	user = auth.authenticate(
		username=username,
		password=password
	)
	if user is not None:
		auth.login(request, user)
	
	return user

def logout(request):
	auth.logout(request)

def register(username, first_name, last_name, email, password):
	# Create Django User
	user = User()
	user.username = username
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.set_password(password)
	user.save()
	return user
