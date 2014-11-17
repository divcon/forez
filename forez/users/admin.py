# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import GardenUser, UserApp


class GardenUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation",
                                widget=forms.PasswordInput)

    class Meta:
        model = GardenUser
        fields = ("email", "username", "phone", 'real_name',
                  'class_num', 'gender')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and (password1 != password2):
            msg = "Passwords don't match"
            raise forms.ValidationError(msg)
        return password2

    def save(self, commit=True):
        user = super(GardenUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class GardenUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = GardenUser
        fields = ('email', 'username', 'phone', 'is_activate',
                  'is_admin', 'real_name', 'class_num', 'gender', 'profile_pic')

    def clean_password(self):
        return self.initial["password"]


class GardenUserAdmin(UserAdmin):
    add_form = GardenUserCreationForm
    form = GardenUserChangeForm

    #can see query
    list_display = ("username", "email", "is_staff", "phone",
                    'real_name', 'class_num', 'gender', 'profile_pic')
    list_filter = ("is_staff", "is_superuser", "is_activate", "groups")
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "phone", 'real_name', 'class_num',
                                      'gender', 'profile_pic')}),
        ("Permissions", {"fields": ("is_activate",
                                    "is_staff",
                                    "is_superuser",
                                    "groups",
                                    "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "phone", "email", "real_name", "class_num",
                       "gender", 'profile_pic', "password1", "password2")
        }),
    )


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('client', 'user')
    raw_id_fields = ('user',)
    ordering = ('client',)


admin.site.register(UserApp, UserAppAdmin)
admin.site.register(GardenUser, GardenUserAdmin)
