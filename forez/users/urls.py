# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import UserViewSet, UserCreateViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = router.urls