# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import UserViewSet, UserCreateViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserCreateViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
