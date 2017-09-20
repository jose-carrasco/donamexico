# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from services.models import Location, Type, Card


class TypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'info', 'publish_date']
    fieldsets = [
        (None, {'fields': ['info', 'publish_date']}),
    ]


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'details', 'publish_date']
    fieldsets = [
        (None, {'fields': ['info', 'details', 'publish_date']}),
    ]


class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'info', 'type', 'location', 'publish_date']
    fieldsets = [
        (None, {'fields': ['title', 'info', 'type', 'location', 'link', 'publish_date']}),
    ]

admin.site.register(Location, LocationAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Card, CardAdmin)
