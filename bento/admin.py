# coding: utf-8

from django.contrib import admin

from bento.models import Recette, Commentaires, Vote

admin.site.register(Recette)
admin.site.register(Commentaires)
admin.site.register(Vote)
