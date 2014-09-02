# -*- coding: utf-8 -*-
from rest_framework import routers
from views import TokensViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'tokens', TokensViewSet)
urlpatterns = router.urls