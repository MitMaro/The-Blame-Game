from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	error_css_class = 'error'
	username = forms.RegexField(
		required=True,
		regex=r"^[a-z][a-z0-9-_]+[a-z0-9]$",
		label="Username",
		min_length=3,
		max_length=30,
		error_messages= {
			'required': "Username is required",
			'invalid': "Username contained invalid characters",
			'min_length': "Username must contain at least 3 characters",
			'max_length': "Username cannot contain more than 18 characters"
		}
	)
	password = forms.CharField(
		required=True,
		label="Password",
		widget=forms.PasswordInput,
		error_messages= {
			'required': "Password is required",
		}
	)
	
class RegisterForm(forms.Form):
	error_css_class = 'error'
	username = forms.RegexField(
		required=True,
		regex=r"^[a-z][a-z0-9-_]+[a-z0-9]$",
		label="Username",
		min_length=3,
		max_length=30,
		error_messages= {
			'required': "Username is required",
			'invalid': "Username contained invalid characters",
			'min_length': "Username must contain at least 3 characters",
			'max_length': "Username cannot contain more than 18 characters"
		}
	)
	
	password = forms.CharField(
		required=True,
		label="Password",
		widget=forms.PasswordInput,
		error_messages= {
			'required': "Password is required",
		}
	)
	
	confirm_password = forms.CharField(
		required=False,
		label="Confirm Password",
		widget=forms.PasswordInput,
	)
	
	firstname = forms.CharField(
		required=True,
		label="First Name",
		max_length=30,
		error_messages= {
			'required': "First name is required",
			'max_length': "Last name cannot contain more than 30 characters"
		}
	)
	
	lastname = forms.CharField(
		required=True,
		label="Last Name",
		max_length=30,
		error_messages= {
			'required': "Username is required",
			'max_length': "Username cannot contain more than 30 characters"
		}
	)
	
	email = forms.EmailField(
		required=True,
		label="Email",
		error_messages= {
			'required': "Email is required",
			'invalid': "Email contained invalid characters",
		}
	)
	
	class Meta:
		model = User
		fields = ("username",)
	
	def clean_confirm_password(self):
		password = self.cleaned_data.get("password", "")
		password_confirm = self.cleaned_data["confirm_password"]
		if password != password_confirm:
			raise forms.ValidationError("The two password fields didn't match.")
		return password_confirm
	
	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("A user with that username already exists.")
	
	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("A user with that email is already registered.")
		
