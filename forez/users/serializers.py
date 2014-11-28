# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import GardenUser
from clients.models import GardenClient


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'password', 'email',
                  'phone', 'real_name', 'class_num', 'gender')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'email', 'phone', 'real_name',
                  'class_num', 'gender', 'password')
        lookup_field = 'username'
        read_only_fields = ('username', 'real_name', 'class_num', 'gender')
        write_only_fields = ('password',)

    def get_profile_url(self):
        return GardenUser.profile_pic

    def change_password(self):
        pass


class UserFindSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'real_name', 'profile_img', 'class_num')


class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GardenClient
        fields = ('name', 'url', 'display_name')