#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from users.models import GardenUser, UserApp
from clients.models import GardenClient


class UserAccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'email', 'phone', 'real_name',
                  'class_num', 'gender', 'profile_img')


class UserClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GardenClient
        fields = ('client_name', 'display_name', 'url',
                  'category', 'short_description', 'app_icon')



# user = models.ForeignKey(AUTH_USER_MODEL)
#     code = models.CharField(max_length=255, db_index=True)  # code comes from oauthlib
#     application = models.ForeignKey(oauth2_settings.APPLICATION_MODEL)
#     expires = models.DateTimeField()
#     redirect_uri = models.CharField(max_length=255)
#     scope = models.TextField(blank=True)