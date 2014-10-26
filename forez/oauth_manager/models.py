# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from provider.oauth2.models import Client
from django.db import models


#contains client details
class GardenClient(Client):
    client_name = models.CharField(max_length=255, blank=True, unique=True)

    # objects = ClientManager()