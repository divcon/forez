# -*- coding: utf-8 -*-

from rest_framework import routers
from .views import AuthorizationViewSet
from django.conf.urls import patterns, url

# router = routers.SimpleRouter(trailing_slash=False)
#
# router.register(r'oauths/authorize', AuthorizationViewSet)
#
# urlpatterns = router.urls

urlpatterns = patterns(
    '',
    url(r'^oauths/authorize/$', AuthorizationViewSet.as_view(), name="authorize"),
)

