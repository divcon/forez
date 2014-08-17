# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import GardenUser


class GardenUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation",
                                widget=forms.PasswordInput)

    class Meta:
        model = GardenUser
        fields = ("email", "username", "phone")

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
        fields = ('email', 'username', 'phone', 'is_activate', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


# class GardenUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = get_user_model()
#
#
# class GardenUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = get_user_model()
#
#     def clean_username(self):
#         username = self.cleaned_data["username"]
#         try:
#             get_user_model().objects.get(username=username)
#         except get_user_model().DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])


class GardenUserAdmin(UserAdmin):
    add_form = GardenUserCreationForm
    form = GardenUserChangeForm

    #can see query
    list_display = ("username", "email", "is_staff", "phone",)
    list_filter = ("is_staff", "is_superuser", "is_activate", "groups")
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "phone")}),
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
            "fields": ("username", "phone", "email", "password1", "password2")
        }),
    )

admin.site.register(GardenUser, GardenUserAdmin)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
#
# from users.models import GardenUser
#
#
# class GardenUserInline(admin.StackedInline):
#     model = GardenUser
#     can_delete = False
#     verbose_name_plural = 'GardenUser'
#
#
# class UserAdmin(UserAdmin):
#     inlines = (GardenUserInline, )
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)