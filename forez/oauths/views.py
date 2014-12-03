#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from oauth2_provider.views.base import AuthorizationView, TokenView
from django.contrib.sessions.models import Session
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.response import Response
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from users.models import GardenUser, UserApp, UserSessionMapper
from teams.models import Team
from .serializers import UserAccountSerializer, UserClientSerializer
from rest_framework.decorators import action
from forez  import settings
import socket


# as_view로 구현해보자
class UserAccountViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    model = GardenUser
    serializer_class = UserAccountSerializer
    required_scopes = ['read']

    def initial(self, request, *args, **kwargs):
        super(UserAccountViewSet, self).initial(request, *args, **kwargs)
        user_obj = request.user
        session_key = request.session.session_key
        print user_obj
        print session_key
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def list(self, request, *args, **kwargs):
        user_obj = request.user
        serializer = UserAccountSerializer(user_obj)
        host_addr = "http://" + request.get_host()
        serializer.data['profile_img'] = host_addr + settings.MEDIA_URL + serializer.data['profile_img']
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOauthViewSet(viewsets.GenericViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    model = Team
    # serializer_class = UserProjectSerializer
    required_scopes = ['read']
    lookup_field = 'username'

    def initial(self, request, *args, **kwargs):
        super(UserOauthViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    @action(['GET'])
    #bug 확인좀....
    def projects(self, request, username=None):
        user_obj = request.user
        if not (user_obj.username == username):
            return Response(data={"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        project_serializer_list = self._make_client_list(target_model=Team, user_obj=user_obj)
        data = {"projects": project_serializer_list}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(['GET'])
    #bug 확인좀...
    def apps(self, request, username=None):
        user_obj = request.user
        if not (user_obj.username == username):
            return Response(data={"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        app_serializer_list = self._make_client_list(target_model=UserApp, user_obj=user_obj)
        data = {'apps': app_serializer_list}
        return Response(data=data, status=status.HTTP_200_OK)

    def _make_client_list(self, target_model, user_obj):
        if target_model is Team:
            target_list = target_model.objects.all().filter(member=user_obj)
        else:
            target_list = target_model.objects.all().filter(user=user_obj)
        client_serializer_list = list()
        for target in target_list:
            client_serializer_list.append(UserClientSerializer(target.client).data)
        return client_serializer_list


class GardenAuthorizationView(AuthorizationView):
    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        session_obj_list = Session.objects.all().filter(session_key=session_key)
        for session_obj in session_obj_list:
            UserSessionMapper.objects.create(user=request.user, session=session_obj)
        return super(GardenAuthorizationView, self).get(request, *args, **kwargs)


class GardenTokenView(TokenView):
    pass


