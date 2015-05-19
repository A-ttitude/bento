# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


DifficulteRecette = (
    (1, _('Novice')),
    (2, _('Facile')),
    (3, _('Moyen')),
    (4, _('Difficile')),
    (5, _('Expert')),
)


CategorieRecette = (
    (1, _('Entrée')),
    (2, _('Plat')),
    (3, _('Dessert')),
    (4, _('Apéritif')),
    (5, _('Fromage')),
    (6, _('Viande')),
    (7, _('Poisson')),
    (8, _('Fruit')),
)


class Ingredients(models.Model):
    nom_i = models.CharField(max_length=100, verbose_name=_("Ingrédient"))

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")


class TypeRecette(models.Model):
    type_r = models.CharField(max_length=25, verbose_name=_("Catégorie"))

    class Meta:
        verbose_name = _("TypeRecette")
        verbose_name_plural = _("TypeRecettes")


class Recette(models.Model):
    titre = models.CharField(max_length=255, verbose_name=_("Titre recette"))
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    type = models.PositiveSmallIntegerField(choices=CategorieRecette)
    difficulte = models.PositiveSmallIntegerField(choices=DifficulteRecette)
    cout = models.PositiveIntegerField(verbose_name=_("Coût"))
    temps_preparation = models.TimeField(verbose_name=_("Temps de préparation"))
    temps_cuisson = models.TimeField(verbose_name=_("Temps de cuisson"))
    temps_repos = models.TimeField(verbose_name=_("Temps de repos"), blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredients, verbose_name=_("Ingrédients"))
    etape = models.TextField(verbose_name=_("Etapes"))
    note_moyenne = models.PositiveIntegerField(verbose_name=_("Note obtenue"))
    photo = models.ImageField(verbose_name=_("Photos"), blank=True, null=True)

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
