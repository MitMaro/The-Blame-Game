from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
	(r'^login/$', 'login'),
	(r'^logout/$', 'logout'),
	(r'^register/$', 'register'),
)
