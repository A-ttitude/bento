# coding: utf-8

from decimal import Decimal

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

DifficulteRecette = (
    (1, _('Novice')),
    (2, _('Facile')),
    (3, _('Moyen')),
    (4, _('Difficile')),
    (5, _('Expert')),
)

CategorieRecette = (
    (1, _('Apéritif')),
    (2, _('Entrée')),
    (3, _('Plat')),
    (4, _('Dessert')),
    (5, _('Légume')),
    (6, _('Poisson')),
    (7, _('Viande')),
    (8, _('Fromages')),
    (9, _('Fruits')),
)


class Recette(models.Model):
    titre = models.CharField(max_length=255, verbose_name=_("Titre recette"))
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    type = models.PositiveSmallIntegerField(choices=CategorieRecette)
    difficulte = models.PositiveSmallIntegerField(choices=DifficulteRecette)
    cout = models.DecimalField(verbose_name=_("Coût"), decimal_places=2, max_digits=12,
                               validators=[MinValueValidator(Decimal('0.00'))])
    temps_preparation = models.TimeField(verbose_name=_("Temps de préparation"))
    temps_cuisson = models.TimeField(verbose_name=_("Temps de cuisson"))
    temps_repos = models.TimeField(verbose_name=_("Temps de repos"))
    ingredients = models.TextField(verbose_name=_("Ingrédients"))
    etape = models.TextField(verbose_name=_("Etapes"))
    note_moyenne = models.PositiveSmallIntegerField(verbose_name=_("Note obtenue"), default=0)
    photo = models.TextField(verbose_name=_("Photos"))
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _("Recette")
        verbose_name_plural = _("Recettes")


class Commentaires(models.Model):
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    recette = models.ForeignKey(Recette, verbose_name=_("Recette"))
    contenu = models.TextField(verbose_name=_("Contenu"))

    def __str__(self):
        return '[' + self.recette.titre + '] [' + self.auteur.username + '] ' + self.contenu

    class Meta:
        verbose_name = _("Commentaire")
        verbose_name_plural = _("Commentaires")


class Vote(models.Model):
    utilisateur = models.ForeignKey(User, verbose_name=_("Utilisateur"))
    recette = models.ForeignKey(Recette, verbose_name=_("Recette"))

    def __str__(self):
        return self.utilisateur.username + ' | ' + self.recette.titre

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
