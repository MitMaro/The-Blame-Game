from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField("the teams name", max_length=128, unique=True)
	users = models.ManyToManyField(User)
	
	def __unicode__(self):
		return self.name

class Point(models.Model):
	team = models.ForeignKey(Team)
	blame = models.ForeignKey(User, related_name="BlamePoint")
	fixer = models.ForeignKey(User, related_name="FixerPoint")
	name = models.CharField("point name", max_length=128, unique=True)
	
	def __unicode__(self):
		return self.name