# -*- coding: utf-8 -*-
from provider.oauth2.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ('name', 'url', 'redirect_uri', 'client_type')
        lookup_field = 'name'