# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import ClientViewSet, ClientCreateViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'clients', ClientCreateViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = router.urls
