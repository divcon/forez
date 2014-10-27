# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import TeamViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'teams', TeamViewSet)

urlpatterns = router.urls
