# -*- coding: utf-8 -*-

from rest_framework import routers
from .views import UserOauthViewSet
# from .views import UserOauthViewSet
from django.conf.urls import patterns, url, include



    # url(r'^oauths/token/$', AuthorizationViewSet.as_view(), name="token"),
    # url(r'^api/v1/users', UserOauthViewSet.as_view(), name="token"),

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'api/v1/users', UserOauthViewSet)
# router.register(r'api/v1/me', MeOauthViewSet.as_view())

urlpatterns = router.urls

#must solve trailing_slash problem
urlpatterns = patterns(
    '',
    url('^', include(router.urls))
    # url(r'^oauths/authorize/$', AuthorizationViewSet.as_view(), name="authorize"),
)