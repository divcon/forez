# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from provider.oauth2.models import Client
from django.db import models


class ClientManager(models.Manager):
    def get_client_obj(self, client_name):
        obj = self.get(name=client_name)
        return obj


#contains client details
class GardenClient(Client):
    client_name = models.CharField(max_length=255, blank=True, unique=True)

    objects = ClientManager()
