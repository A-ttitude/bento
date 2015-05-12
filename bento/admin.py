#coding: utf-8

from django.contrib import admin
from bento.models import Ingredients, DifficulteRecette, TypeRecette, Recette, Commentaires


admin.site.register(Recette)
admin.site.register(TypeRecette)
admin.site.register(Commentaires)
admin.site.register(Ingredients)


#class UserAdmin(admin.ModelAdmin):
#   list_filter = ('nickname',)
#    date_hierarchy = 'date'