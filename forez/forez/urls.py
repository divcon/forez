# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forez.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tokens.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('oauth_manager.urls')),
    # url(r'^', include('teams.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include('redirects.urls')),
)
