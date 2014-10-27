#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from teams.models import Team
from rest_framework.decorators import action
from users.models import GardenUser
from oauth_manager.models import GardenClient


class TeamViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    model = Team
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'client'

    def initial(self, request, *args, **kwargs):
        super(TeamViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def list(self, request, *args, **kwargs):
        """
            Listing teams(apps)
        """
        clients_list = Team.objects.all().filter(member=request.user.username)
        result_list = list()
        for c in clients_list:
            tmp_dict = dict()
            tmp_dict['client'] = c.client.name
            tmp_dict['owner'] = Team.objects.get_team_owner(c.client).member.username
            result_list.append(tmp_dict)

        return Response(data=result_list, status=status.HTTP_200_OK)

    @action(['POST', 'GET'])
    def members(self, request, client=None):
        client_obj = GardenClient.objects.get_client_obj(client)

        #chage to function
        #check member
        if not Team.objects.is_member(request.user, client_obj):
            return Response(data={'Error': 'No Authentication'}, status=status.HTTP_401_UNAUTHORIZED)

        #_post_member
        if request.method == 'POST':
            if GardenUser.objects.is_exist(username=request.DATA['member']):
                member_obj = GardenUser.objects.get_user_obj(request.DATA['member'])
                tmp_dict = dict()
                tmp_dict['client'] = client_obj
                tmp_dict['member'] = member_obj
                Team.objects.add_team_member(tmp_dict)
                return Response(data={'OK': 'add member'}, status=status.HTTP_201_CREATED)
            return Response(data={'Error': 'Check user name'}, status=status.HTTP_409_CONFLICT)
        #_get_member
        if request.method == 'GET':
            member_list = Team.objects.get_team_members(client_obj)
            return Response(data=member_list, status=status.HTTP_200_OK)