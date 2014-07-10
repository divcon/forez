# -*- coding: utf-8 -*-

from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status, generics
from django.contrib.auth.models import User
from serializers import *
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (UnicodeJSONRenderer, )

    def retrieve(self, request, *args, **kwargs):
        serializer = UserSerializer()

    def list(self, request, pk=None):
        # if queryset is None:
        serializer = UserSerializer(self.queryset, many=True, context={'request': request})

        return Response(serializer.data)


class UserCreateViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (UnicodeJSONRenderer, )

    def initial(self, request, *args, **kwargs):
        super(UserCreateViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def create(self, request, *args, **kwargs):
        #When 'context deprecated' error occurs, add context parameter.
        serializer = UserCreateSerializer(data=request.DATA, context={'request': request})
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
                email=serializer.data['email'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print serializer.errors

            if 'username' in serializer.errors:
                username_error = serializer.errors.get('username', None)
                if username_error == [u'User with this Username already exists.']:
                    return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)



    # def create(self, request, *args, **kwargs):