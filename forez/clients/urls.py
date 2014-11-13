# -*- coding: utf-8 -*-
from rest_framework import routers
from .views import ClientViewSet, StoreViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'clients', ClientViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = router.urls
