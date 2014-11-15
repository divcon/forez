# -*- coding: utf-8 -*-

from .models import GardenClient
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenClient
        fields = ('name', 'url', 'redirect_uris', 'client_type', 'client_id',
                  'client_secret', 'authorization_grant_type')
        lookup_field = 'name'
        read_only_fields = ('name', 'client_type', 'client_id', 'client_secret')

     # create app detail when registering clients.
    def init_app_detail(self):
        pass

    def init_teams(self):
        pass


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GardenClient
        fields = ('tag1', 'tag2', 'tag3', 'category', 'short_description',
                  'long_description', 'permission_explanation')
        lookup_field = 'name'


class SettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GardenClient
        fields = ('display_name', 'contact_email', 'publish', 'created_at')
        lookup_field = 'name'


class ClientCreateSerializer(serializers.ModelSerializer):
    team = serializers.RelatedField(many=False)

    class Meta:
        model = GardenClient
        fields = ('name', 'url', 'redirect_uris', 'client_type', 'authorization_grant_type')

    # def is_valid(self):
    #     if super(ClientCreateSerializer, self).is_valid():
    #         _errors = dict()
    #         if GardenClient.objects.filter(name=self.object.name).exists():
    #             _errors['name'] = ['Application name is already exist.']
    #             self._errors = _errors
    #             return False
    #
    #         return True


class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GardenClient
        #app_icon add
        fields = ('display_name', 'category', 'url', 'contact_email',
                  'short_description', 'long_description',
                  'permission_explanation', 'tag1', 'tag2', 'tag3', 'created_at')

