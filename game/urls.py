from django.conf.urls.defaults import *

urlpatterns = patterns('game.views',
	url(r'^$', 'index', name="game-index"),
	(r'^score/(\d+)/$', 'score'),
	(r'^add/(\d+)/$', 'add')
)
