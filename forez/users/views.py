# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status, generics
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
        data = dict()
        request_user = GardenUser.objects.get(username=request.user)
        request_user.email = request.DATA['email']
        request_user.phone = request.DATA['phone']
        if not request.DATA['password'] == "":
            request_user.set_password(request.DATA['password'])
            data['password'] = 'changed'
        request_user.save()
        data['email'] = request_user.email
        data['phone'] = request_user.phone
        return Response(data=data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
            Leaving from Garden Platform
        """
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super(UserViewSet, self).destroy(request, *args, **kwargs)


class UserCreateViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
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

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = GardenUser.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
            return queryset
        return queryset

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
                    return Response(data={'error': 'username is already exists.'}, status=status.HTTP_409_CONFLICT)
                    # return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            elif 'email' in serializer.errors:
                return Response(data={'error': 'email is already exists'}, status=status.HTTP_409_CONFLICT)
                # return Response(serializer._errors, status=status.HTTP_409_CONFLICT)

            return Response(data={'error': 'username is already exists.'}, status=status.HTTP_409_CONFLICT)
            # return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        query_result = self.get_queryset()
        if query_result:
            data = {"error": "ID is already exists"}
            return Response(data, status=status.HTTP_409_CONFLICT)
        data = {"OK": "Can use ID"}
        return Response(data, status=status.HTTP_200_OK)