#coding: utf-8

from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_filter = ('nickname',)
    date_hierarchy = 'date'