# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from clients.models import GardenClient

from django.contrib.sessions.models import Session
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class GardenUserManager(BaseUserManager):
    def create_user(self, form):
        user = self.model(
            email=GardenUserManager.normalize_email(form['email']),
            username=form['username'],
            real_name=form['real_name'],
            phone=form['phone'],
            class_num=form['class_num'],
            gender=form['gender'],
        )
        user.set_password(form['password'])
        user.save(using=self._db)

        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(kwargs)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def is_exist(self, username):
        if self.all().filter(username=username):
            return True
        return False

    def get_user_obj(self, username):
        return self.get(username=username)


class GardenUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        db_index=True,
        null=True,
        default='your@email.com'
    )
    #user_id
    username = models.CharField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=15, blank=False)
    real_name = models.CharField(max_length=50, blank=False)
    class_num = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=5, blank=False)
    id = models.AutoField(primary_key=True)
    #need add
    # birth = models.DateField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile/custom',
                                    default='profile/GardenUserDefault.png')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "real_name", "class_num", "gender"]

    #disabled
    is_activate = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = GardenUserManager()

    def get_full_name(self):
        return "%s" % self.username

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.username


class UserAppManager(models.Manager):
    def is_already_registering(self, user_obj, client_obj):
        queryset = self.all().filter(user=user_obj, client=client_obj)
        if queryset.__len__() > 0:
            return True
        return False

    def get_app_list(self, user_obj):
        queryset = self.all().filter(user=user_obj)
        app_list = list()
        for q in queryset:
            app_list.append(q.client)
        print app_list
        return app_list


class UserApp(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    client = models.ForeignKey(GardenClient, related_name='application', null=False, to_field='client_name')
    user = models.ForeignKey(GardenUser, related_name='user', null=False, to_field='username')
    objects = UserAppManager()

    class Meta:
        # unique_together = ('client', 'user')
        pass


class MapperManager(models.Manager):
    def get_session_obj(self, user_obj):
        return self.all().filter(user=user_obj)


class UserSessionMapper(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(GardenUser, related_name='GardenUser', null=False, to_field='username')
    session = models.ForeignKey(Session, related_name='session',
                                null=False, to_field='session_key')
    objects = MapperManager()