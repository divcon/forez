# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from forez.settings import MEDIA_ROOT, STATIC_ROOT
# from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forez.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tokens.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('clients.urls')),
    url(r'^', include('teams.urls')),
    url(r'^', include('oauths.urls')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^o/', include('oauths.urls', namespace='oauths')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^', include('redirects.urls')),
)
urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': MEDIA_ROOT}))
urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': STATIC_ROOT}))