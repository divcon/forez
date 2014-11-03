# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from users.models import GardenUser
from oauth_manager.models import GardenClient


class TeamManager(models.Manager):

    def create_team(self, client, member, is_owner=False):
        team = self.create(client=client, member=member, is_owner=is_owner)
        return team

    def get_team_owner(self, client):
        leader = self.get(client=client, is_owner=True)
        return leader

    def add_team_member(self, member_info):
        client = member_info['client']
        member = member_info['member']
        team_member = self.create(client=client, member=member, is_owner=False)
        print "new member is added"
        return team_member

    def get_team_members(self, client):
        team_members = list()
        queryset = self.all().filter(client=client)
        for q in queryset:
            tmp_dict = dict()
            tmp_dict['member'] = q.member.username
            tmp_dict['is_owner'] = q.is_owner
            team_members.append(tmp_dict)
        return team_members

    def is_member(self, user_obj, client_obj):
        queryset = self.all().filter(member=user_obj, client=client_obj)
        if queryset.__len__() > 0:
            return True
        return False


class Team(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    client = models.ForeignKey(GardenClient, related_name='client', null=False, to_field='client_name')
    member = models.ForeignKey(GardenUser, related_name='member', null=False, to_field='username')
    is_owner = models.BooleanField(null=False, blank=False, default=False)
    objects = TeamManager()

    class Meta:
        unique_together = ('client', 'member')