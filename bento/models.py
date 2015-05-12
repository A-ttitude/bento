# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    nom_i = models.CharField(max_length=100, verbose_name=_("Ingrédient"))

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")


DifficulteRecette = (
    (1, 'Novice'),
    (2, 'Facile'),
    (3, 'Moyen'),
    (4, 'Difficile'),
    (5, 'Expert'),
)


class TypeRecette(models.Model):
    type_r = models.CharField(max_length=25, verbose_name=_("Catégorie"))

    class Meta:
        verbose_name = _("TypeRecette")
        verbose_name_plural = _("TypeRecettes")


class Recette(models.Model):
    titre = models.CharField(max_length=255, verbose_name=_("Titre recette"))
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    type = models.OneToOneField(TypeRecette, verbose_name=_("Type"))
    difficulte = models.IntegerField(choices=DifficulteRecette, max_length=1)
    cout = models.PositiveIntegerField(verbose_name=_("Coût"))
    temps_preparation = models.TimeField(verbose_name=_("Temps de préparation"))
    temps_cuisson = models.TimeField(verbose_name=_("Temps de cuisson"))
    temps_repos = models.TimeField(verbose_name=_("Temps de repos"), null=True)
    ingredients = models.ManyToManyField(Ingredients, verbose_name=_("Ingrédients"))
    etape = models.TextField(verbose_name=_("Etapes"))
    note_moyenne = models.PositiveIntegerField(verbose_name=_("Note obtenue"))
    photo = models.ImageField(verbose_name=_("Photos"))

    class Meta:
        verbose_name = _("Recette")
        verbose_name_plural = _("Recettes")


class Commentaires(models.Model):
    titre_c = models.CharField(max_length=500, verbose_name=_("Titre"))
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    recette = models.ForeignKey(Recette, verbose_name=_("Recette"))
    contenu = models.TextField(verbose_name=_("Contenu"))

    class Meta:
        verbose_name = _("Commentaire")
        verbose_name_plural = _("Commentaires")



# class Chef(User):
#   nickname = models.CharField(max_length=50)
#   passwd = models.CharField(max_length=50)
#   mail = models.CharField(max_length=100)
#   registryDate = models.DateField(auto_now=True)

#   def __str__(self):
#       return self.nickname

# class Meta:
#   verbose_name = _("Chef")
#   verbose_name_plural = _("Chefs")

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