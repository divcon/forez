#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from teams.models import Team
from .models import GardenClient


class ClientPermission(object):
    def has_permission(self, request, client_name):
        user_obj = request.user
        client_obj = GardenClient.objects.get_client_obj(client_name=client_name)
        return Team.objects.is_member(user_obj=user_obj, client_obj=client_obj)