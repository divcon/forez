# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import hashlib
import time

from django.db import models
from django.db.models import Q
from users.models import GardenUser

#
# class Team(models.Model):
#     id = models.AutoField(primary_key=True)
#     team_name = models.CharField(max_length=255, null=False, unique=True)
#     leader = models.ForeignKey(GardenUser, related_name='team_leader')
#     member2 = models.ForeignKey(GardenUser, relate_name='team_member1', null=True)
#     member3 = models.ForeignKey(GardenUser, relate_name='team_member1', null=True)
#     member4 = models.ForeignKey(GardenUser, relate_name='team_member1', null=True)
#     member5 = models.ForeignKey(GardenUser, relate_name='team_member1', null=True)
#     member6 = models.ForeignKey(GardenUser, relate_name='team_member1', null=True)
#     description = models.CharField(max_length=255, null=True)
#     # optional
#     # team_log
#     # team_board = models.CharField(max_length=255, default='http://teamboard')
#
#     class Meta:
#         pass