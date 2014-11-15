# # -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Team


class RawIDAdmin(admin.ModelAdmin):
    list_display = ('client', 'member', 'is_owner')
    raw_id_fields = ('member',)
    ordering = ('client',)
admin.site.register(Team, RawIDAdmin)