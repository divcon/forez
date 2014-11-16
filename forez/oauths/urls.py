# -*- coding: utf-8 -*-

from rest_framework import routers
from .views import AuthorizationViewSet
from django.conf.urls import patterns, url

# router = routers.SimpleRouter(trailing_slash=False)
#
# router.register(r'oauths/authorize', AuthorizationViewSet)
#
# urlpatterns = router.urls

# must solve trailing_slash problem
urlpatterns = patterns(
    '',
    url(r'^oauths/authorize/$', AuthorizationViewSet.as_view(), name="authorize"),
    url(r'^oauths/token/$', AuthorizationViewSet.as_view(), name="token"),
)

