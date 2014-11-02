# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from provider.oauth2.models import Client
from django.db import models


class ClientManager(models.Manager):
    def get_client_obj(self, client_name):
        obj = self.get(name=client_name)
        return obj

    def is_publish(self, client_name):
        obj = self.get(name=client_name)
        return obj.publish


# class ClientDetailManager(models.Manager):
#     def is_publish(self, client_name):
#         obj = self.get(name=client_name)
#         return obj.publish


#contains client details
class GardenClient(Client):
    client_name = models.CharField(max_length=255, blank=True, unique=True)
    #app_detail
    #      for search
    tag1 = models.CharField(max_length=50, blank=True)
    tag2 = models.CharField(max_length=50, blank=True)
    tag3 = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    #       for description
    short_description = models.CharField(max_length=255, blank=True)
    long_description = models.TextField(blank=True)
    permission_explanation = models.TextField(blank=True)
    #       publishing
    publish = models.BooleanField(default=False)
    #       icon
    # small_icon = models.ImageField(blank=True)
    # app_icon = models.ImageField(blank=True)

    # settings
    display_name = models.CharField(max_length=30, blank=True)
    contact_email = models.EmailField(blank=True)

    # Alert
    # log module is needed
    app_log = models.TextField(blank=True)

    objects = ClientManager()

# class ClientDetail(models.Model):
#     # client = models.ForeignKey()
#     #app_detail
#     #      for search
#     tag1 = models.CharField(max_length=50, blank=True)
#     tag2 = models.CharField(max_length=50, blank=True)
#     tag3 = models.CharField(max_length=50, blank=True)
#     category = models.CharField(max_length=50, blank=True)
#     #       for description
#     short_description = models.CharField(max_length=255, blank=True)
#     long_description = models.TextField(blank=True)
#     permission_explanation = models.TextField(blank=True)
#     #       icon
#     # small_icon = models.ImageField(blank=True)
#     # app_icon = models.ImageField(blank=True)
#     #       publishing
#     publish = models.BooleanField(default=False)
#
#     # settings
#     display_name = models.CharField(max_length=30, blank=True)
#     contact_email = models.EmailField(blank=True)
#
#     # Alert
#     # log module is needed
#     app_log = models.TextField(blank=True)
#
#     objects = ClientManager()
