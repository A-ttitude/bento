# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Chef(User):
    nickname = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    registryDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = _("Chef")
        verbose_name_plural = _("Chefs")



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
#         verbose_name_plural = _("Recettes")