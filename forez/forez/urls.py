# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from users import views as users_views
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forez.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('users.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
