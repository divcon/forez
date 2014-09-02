# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.renderers import UnicodeJSONRenderer

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token


class TokensViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin):
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer, )
    serializer_class = AuthTokenSerializer
    model = Token

    def initial(self, request, *args, **kwargs):
        super(TokensViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.DATA)

        print serializer.is_valid()
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            id_num = serializer.object['user'].id
            return Response({'token': token.key, 'id': id_num})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
