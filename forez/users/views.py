# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from clients.models import GardenClient
from .models import GardenUser, UserApp
from .serializers import UserSerializer, UserCreateSerializer, AppSerializer
from rest_framework.renderers import UnicodeJSONRenderer, JSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from forez.settings import MEDIA_ROOT
from os import path
import os


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
        user_obj = GardenUser.objects.get_user_obj(kwargs['username'])
        serializer = UserSerializer(user_obj)
        serializer.data['profile_img'] = request.user.profile_img.url
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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

    @action(['POST'])
    def icons(self, request, username=None):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            user_obj = request.user

        if request.method == 'POST':
            url = self._save_icon(request, user_obj)
            data = dict()
            data['url'] = url
            return Response(data=data, status=status.HTTP_200_OK)

    @action(['POST', 'GET', 'DELETE'])
    def apps(self, request, username=None):
        if request.user != self.get_object():
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            pass

        if request.method == 'GET':
            app_list = UserApp.objects.get_app_list(request.user)
            data_set = self._make_app_data(app_list)
            return Response(data=data_set, status=status.HTTP_200_OK)

        if request.method == 'POST':
            client_name = request.DATA['client_name']
            client_obj = GardenClient.objects.get_client_obj(client_name)
            if UserApp.objects.is_already_registering(user_obj=request.user, client_obj=client_obj):
                return Response(data={"error": "Already regitering"}, status=status.HTTP_409_CONFLICT)
            if not GardenClient.objects.is_publish(client_obj.name):
                return Response(data={"error": "Application is not available"}, status=status.HTTP_403_FORBIDDEN)
            else:
                UserApp.objects.create(user=request.user, client=client_obj)
                return Response(data=request.DATA, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            delete_app_name = request.QUERY_PARAMS.get('name')
            client_obj = GardenClient.objects.get_client_obj(delete_app_name)
            if UserApp.objects.is_already_registering(user_obj=request.user, client_obj=client_obj):
                UserApp.objects.get(user=request.user, client=client_obj).delete()
                return Response(data={"ok": "Delete ok"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(data={"error": "No app."}, status=status.HTTP_400_BAD_REQUEST)

    def _make_app_serializer_list(self, app_list):
        app_serializer_list = list()
        for a in app_list:
            app_serializer = AppSerializer(a)
            app_serializer.data['app_icon'] = a.app_icon.url
            app_serializer_list.append(app_serializer)
        return app_serializer_list

    def _make_app_data(self, app_list):
        serializer_list = self._make_app_serializer_list(app_list)
        data = list()
        for s in serializer_list:
            data.append(s.data)
        return data

    def _save_icon(self, request, user_obj):
        extends = self._get_file_extends(request)
        self._delete_before_icon(user_obj, extends=extends)
        return self._set_icon(request, user_obj, extends=extends)

    def _delete_before_icon(self, user_obj, extends):
        file_path = MEDIA_ROOT+'/profile/custom/'+user_obj.username+'.'+extends
        if path.exists(file_path):
            print "icon is already registered. delete before icon"
            os.remove(file_path)
        else:
            print user_obj.username + " 's image is changed."

    def _get_file_extends(self, request):
        extends = (request.FILES['icon'].name.split('.')[1]).upper()

        return extends

    def _set_icon(self, request, user_obj, extends):
        file_content = ContentFile(request.FILES['icon'].read())
        user_obj.profile_img.save(user_obj.username+'.'+extends, file_content)
        return user_obj.profile_img.url


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
