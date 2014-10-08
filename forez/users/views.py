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


#combine all class later....(refactoring)
#retrieve another user's info
class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
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
        """
            Inquiring my Information
        """
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            Modifying my Information
        """
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Leaving from Garden Platform
        """
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super(UserViewSet, self).destroy(request, *args, **kwargs)


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
        """
            Join to Garden platform
        """
        #When 'context deprecated' error occurs, add context parameter.
        serializer = UserCreateSerializer(data=request.DATA, context={'request': request})
        if serializer.is_valid():
            join_form = {
                'email': serializer.data['email'],
                'username': serializer.data['username'],
                'real_name': serializer.data['real_name'],
                'phone': serializer.data['phone'],
                'class_num': serializer.data['class_num'],
                'gender': serializer.data['gender'],
                'password': serializer.data['password'],
            }
            # if serializer.data['birth'] is not None:
            #     join_form.update('birth', serializer.data['birth'])
            GardenUser.objects.create_user(join_form)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print serializer.errors

            if 'username' in serializer.errors:
                username_error = serializer.errors.get('username', None)
                if username_error == [u'User with this Username already exists.']:
                    return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            elif 'email' in serializer.errors:
                email_error = serializer.errors.get('email', None)
                return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)



    # def create(self, request, *args, **kwargs):
