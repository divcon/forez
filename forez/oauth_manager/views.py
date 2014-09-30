#-*- coding: utf-8 -*-
from .serializers import ClientSerializer
from provider.oauth2.models import Client
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.renderers import UnicodeJSONRenderer
from rest_framework.authentication import TokenAuthentication


class ClientViewSet():
    model = Client
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UnicodeJSONRenderer, )
    lookup_field = 'user'

    def initial(self, request, *args, **kwargs):
        super(ClientViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def create(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super(ClientViewSet, self).retrieve(request, *args, **kwargs)
