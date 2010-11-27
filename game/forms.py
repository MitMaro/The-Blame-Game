from django.forms import ModelForm
from models import Point

class AddPointForm(ModelForm):
	error_css_class = 'error'
	class Meta:
		model = Point
		fields = ('name', 'blame', 'fixer')
