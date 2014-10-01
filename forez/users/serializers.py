# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GardenUser


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'password', 'email',
                  'phone', 'real_name', 'class_num', 'gender')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'email', 'phone', 'real_name',
                  'class_num', 'gender', 'profile_pic')
        lookup_field = 'username'
