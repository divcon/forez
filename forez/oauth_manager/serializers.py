# -*- coding: utf-8 -*-
from provider.oauth2.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ('name', 'url', 'redirect_uri', 'client_type', 'client_id', 'client_secret')
        lookup_field = 'name'
        read_only_fields = ('name', 'client_type', 'client_id', 'client_secret')

    def is_valid(self):
        if super(ClientSerializer, self).is_valid():
            _errors = dict()
            if Client.objects.filter(name=self.object.name).exists():
                _errors['name'] = ['Application name is already exist.']
                self._errors = _errors
                return False

            return True

    # create app detail when registering clients.
    def init_app_detail(self):
        pass
