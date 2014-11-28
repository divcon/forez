# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import UserViewSet, UserCreateViewSet, UserFindViewSet
# from .views import PasswordViewSet
from django.conf.urls import patterns, url, include

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserCreateViewSet)
router.register(r'users', UserViewSet)
router.register(r'search', UserFindViewSet)

#tmp url. don't use this url
# router.register(r'password', PasswordViewSet)

# urlpatterns = router.urls
urlpatterns = patterns(
    '',
    url('^', include(router.urls)),
)