# #-*- coding: utf-8 -*-
#
# from __future__ import unicode_literals
# from django.contrib.sessions.models import Session
# from django.db import models
# from users.models import GardenUser
#
#
# class MapperManager(models.Manager):
#     def get_session_key(self, user_obj):
#         return self.all().fileter(user=user_obj)
#
#
# class UserSessionMapper(models.Model):
#     id = models.AutoField(primary_key=True, null=False, blank=False)
#     user = models.ForeignKey(GardenUser, related_name='user', null=False, to_field='username')
#     session = models.ForeignKey(Session, related_name='session', null=False, to_field='session_key')
#     objects = MapperManager()