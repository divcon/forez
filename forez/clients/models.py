# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

from oauth2_provider.models import AbstractApplication


class ClientManager(models.Manager):
    def get_client_obj(self, client_name):
        obj = self.get(name=client_name)
        return obj

    def is_publish(self, client_name):
        obj = self.get(name=client_name)
        return obj.publish

    def already_exist(self, client_name):
        queryset = self.all().filter(name=client_name)
        if queryset.__len__() > 0:
            return True
        return False


#contains client details
class GardenClient(AbstractApplication):
    client_name = models.CharField(max_length=255, blank=True, unique=True)
    #       icon
    app_icon = models.ImageField(upload_to='app_icon/custom',
                                 default='app_icon/GardenPlatformDefault.png')
    url = models.URLField(max_length=255)
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

    # settings
    display_name = models.CharField(max_length=30, blank=True)
    contact_email = models.EmailField(blank=True)
    created_at = models.DateField(auto_now=True)

    # Alert
    # log module is needed
    app_log = models.TextField(blank=True)

    objects = ClientManager()

    # _icon_dir = str
    #
    # @property
    # def icon_dir
