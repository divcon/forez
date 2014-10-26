# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import hashlib
import time

from django.db import models
from django.db.models import Q
from users.models import GardenUser
from oauth_manager.models import GardenClient
from provider.oauth2.models import Client


class TeamManager(models.Manager):

    def create_team(self, client, member, is_owner=False):
        team = self.create(client=client, member=member, is_owner=is_owner)
        return team

    def get_team_owner(self, team_name):
        leader = self.get(team_name=team_name, is_owner=True)
        return leader

    def add_team_member(self, member_info):
        team_member = self.create(client=member_info['client'], member=['member'], is_owner=False)
        print "new member is added"
        return team_member

    # go to views
    #
    # def is_exist(self, username):
    #     """
    #         True : exist
    #         False : not Exist
    #     """
    #     if GardenUser.objects.get(username=username) is not None:
    #         return True
    #     return False


class Team(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    client = models.ForeignKey(GardenClient, related_name='project', null=False, to_field='client_name')
    member = models.ForeignKey(GardenUser, related_name='member', null=False, to_field='username')
    is_owner = models.BooleanField(null=False, blank=False, default=False)
    objects = TeamManager()

    class Meta:
        unique_together = ('client', 'member')