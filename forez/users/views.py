# -*- coding: utf-8 -*-

from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status, generics
from django.contrib.auth.models import User
from .models import GardenUser
from serializers import *
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer, JSONRenderer
from users import models
from rest_framework.authentication import TokenAuthentication


#retrieve another user's info
class UserViewSet(viewsets.ModelViewSet):
    model = GardenUser
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UnicodeJSONRenderer, )
    lookup_field = 'username'

    def initial(self, request, *args, **kwargs):
        super(UserViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def retrieve(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super(UserViewSet, self).retrieve(request, *args, **kwargs)


#retrieve my info
# class MyInfoViewSet(viewsets.GenericViewSet,
#                     mixins.RetrieveModelMixin):
#     model = GardenUser
#     serializer_class = UserSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     renderer_classes = (UnicodeJSONRenderer, )
#     lookup_field = 'username'
#
#     def initial(self, request, *args, **kwargs):
#         super(MyInfoViewSet, self).initial(request, *args, **kwargs)
#         if isinstance(request.DATA, dict):
#             for key in request.DATA.keys():
#                 if type(request.DATA[key]) is list:
#                     request.DATA[key] = request.DATA[key][0]
#
#     def retrieve(self, request, *args, **kwargs):
#         if request.user != self.get_object():
#             return Response(status=status.HTTP_403_FORBIDDEN)
#
#         return super(MyInfoViewSet, self).retrieve(request, *args, **kwargs)


class UserCreateViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin):
    permission_classes = (AllowAny, )
    # model = User
    # queryset = User.objects.all()
    model = GardenUser
    queryset = GardenUser.objects.all()
    serializer_class = UserCreateSerializer
    renderer_classes = (UnicodeJSONRenderer, JSONRenderer,)

    def initial(self, request, *args, **kwargs):
        super(UserCreateViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def create(self, request, *args, **kwargs):
        #When 'context deprecated' error occurs, add context parameter.
        serializer = UserCreateSerializer(data=request.DATA, context={'request': request})
        print request
        if serializer.is_valid():
            GardenUser.objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
                email=serializer.data['email'],
                phone=serializer.data['phone'],)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print serializer.errors

            if 'username' in serializer.errors:
                username_error = serializer.errors.get('username', None)
                if username_error == [u'User with this Username already exists.']:
                    return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)



    # def create(self, request, *args, **kwargs):
