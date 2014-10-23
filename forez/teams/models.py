# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import hashlib
import time

from django.db import models
from django.db.models import Q
from users.models import GardenUser
from provider.oauth2.models import Client


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='project_name', null=False, unique=True)
    member = models.ForeignKey(GardenUser, related_name='team_member')
    is_owner = models.BooleanField(null=False)
    # optional
    # team_log
    # team_board = models.CharField(max_length=255, default='http://teamboard')

    class Meta:
        pass

    def add_member(self):
        pass

    def get_leader_name(self, project_id):
        team_leader = self.objects.get(client_id=project_id, is_owner=True)
        return GardenUser.objects.get(id=team_leader.member_id)

    def get_team_members(self, project_id):
        project_list = self.objects.all()
        object_list = project_list.filter(client_id=project_id)
        member_list = list()

        for o in object_list:
            member_id = o.member_id
            name = GardenUser.objects.get(id=member_id).name
            member_list.append(name)
        #for test
        print member_list
        return member_list
