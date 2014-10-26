# -*- coding: utf-8 -*-
from django.db import models

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


class GardenUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        db_index=True,
    )
    #user_id
    username = models.CharField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=15, blank=False)
    real_name = models.CharField(max_length=50, blank=False)
    class_num = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=5, blank=False)

    #need add
    # birth = models.DateField(blank=True, null=True)
    profile_pic = models.CharField(max_length=255,
                                   default="../web_content/resource/images/personal_profile")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "real_name", "class_num", "gender"]

    #disabled
    is_activate = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = GardenUserManager()

    def get_full_name(self):
        return "%s" % (self.username)

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.username

