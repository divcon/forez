# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url 
#from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^main/$', 'redirects.views.login_user'),
)
