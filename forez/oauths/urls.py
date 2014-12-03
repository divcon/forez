# -*- coding: utf-8 -*-

from rest_framework import routers
from .views import UserAccountViewSet, UserOauthViewSet, GardenTokenView, GardenAuthorizationView
from django.conf.urls import patterns, url, include

router = routers.DefaultRouter(trailing_slash=False)
# router = routers.SimpleRouter(trailing_slash=False)

router.register(r'api/v1/users', UserOauthViewSet)
router.register(r'api/v1/me', UserAccountViewSet)

urlpatterns = router.urls

#must solve trailing_slash problem
urlpatterns = patterns(
    '',
    url('^', include(router.urls)),
    url(r'^authorize/$', GardenAuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', GardenTokenView.as_view(), name="token"),
)