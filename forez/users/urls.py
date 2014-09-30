# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import UserViewSet, UserCreateViewSet
#from views import MyInfoViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserCreateViewSet)
router.register(r'users', UserViewSet)
# router.register(r'users/me', MyInfoViewSet)

urlpatterns = router.urls
