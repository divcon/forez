# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class GardenUserManager(BaseUserManager):
    def create_user(self, email, phone, password, username):
        user = self.model(
            email=GardenUserManager.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password, username):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class GardenUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        db_index=True,
    )
    username = models.CharField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=15, blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

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

# class GardenUser(models.Model):
#     class Meta:
#         verbose_name = 'GardenUser'
#         verbose_name_plural = 'GardenUser'
#
#     # user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     user = models.OneToOneField(User)
#     phone = models.CharField(verbose_name='phone', max_length=15, blank=False)

