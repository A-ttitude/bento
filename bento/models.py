# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


# class User(models.Model):
# nickname = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     dateRegistration = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.nickname
#
#     class Meta:
#         verbose_name = _("Utilisateur")
#         verbose_name_plural = _("Utilisateurs")


# class Recipe(models.Model):
#     owner = models.ForeignKey('User')
#     name = models.CharField(max_length=255)
#     note = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = _("Recette")
S#         verbose_name_plural = _("Recettes")