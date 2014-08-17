# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GardenUser


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'password', 'email', 'phone')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenUser
        fields = ('username', 'email', 'phone')
        # lookup_field = 'username'