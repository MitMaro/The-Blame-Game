from django.contrib import admin
from models import Team, Point

class TeamAdmin(admin.ModelAdmin):
	pass
admin.site.register(Team, TeamAdmin)

class PointAdmin(admin.ModelAdmin):
	pass
admin.site.register(Point, PointAdmin)
