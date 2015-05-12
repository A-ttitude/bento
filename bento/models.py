# coding: utf-8

from enum import Enum
from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    nom_i = models.CharField(max_length=100, verbose_name="Ingrédient")


DifficulteRecette = (
    (1, 'Novice'),
    (2, 'Facile'),
    (3, 'Moyen'),
    (4, 'Difficile'),
    (5, 'Expert'),
)


class TypeRecette(models.Model):
    type_r = models.CharField(max_length=25, verbose_name="Catégorie")


class Recette(models.Model):
    titre = models.CharField(max_length=255, verbose_name="Titre recette")
    auteur = models.ForeignKey(User, verbose_name="Auteur")
    type = models.OneToOneField(TypeRecette, verbose_name="Type")
    difficulte = models.IntegerField(choices=DifficulteRecette, max_length=1)
    cout = models.PositiveIntegerField(verbose_name="Coût")
    temps_preparation = models.TimeField(verbose_name="Temps de préparation")
    temps_cuisson = models.TimeField(verbose_name="Temps de cuisson")
    temps_repos = models.TimeField(verbose_name="Temps de repos", null=True)
    ingredients = models.ManyToManyField(Ingredients, verbose_name="Ingrédients")
    etape = models.TextField(verbose_name="Etapes")
    note_moyenne = models.PositiveIntegerField(verbose_name="Note obtenue")
    photo = models.ImageField(verbose_name="Photos")


class Commentaires(models.Model):
    titre_c = models.CharField(max_length=500, verbose_name="Titre")
    auteur = models.ForeignKey(User, verbose_name="Auteur")
    recette = models.ForeignKey(Recette, verbose_name="Recette")
    contenu = models.TextField(verbose_name="Contenu")
































#class Chef(User):
#    nickname = models.CharField(max_length=50)
#    passwd = models.CharField(max_length=50)
#    mail = models.CharField(max_length=100)
#    registryDate = models.DateField(auto_now=True)

 #   def __str__(self):
 #       return self.nickname

#    class Meta:
#        verbose_name = _("Chef")
#        verbose_name_plural = _("Chefs")



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