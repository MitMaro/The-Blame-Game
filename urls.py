from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
	
	(r'^$', include('TheBlameGame.default.urls')),
	
	(r'^accounts/', include('TheBlameGame.accounts.urls')),
	
	(r'^game/', include('TheBlameGame.game.urls')),

	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
)
