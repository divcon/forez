# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'test', UserViewSet)

urlpatterns = router.urls