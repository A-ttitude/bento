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
    (1, _('Entrée')),
    (2, _('Plat')),
    (3, _('Dessert')),
    (4, _('Apéritif')),
    (5, _('Fromage')),
    (6, _('Viande')),
    (7, _('Poisson')),
    (8, _('Fruit')),
)


class Recette(models.Model):
    titre = models.CharField(max_length=255, verbose_name=_("Titre recette"))
    auteur = models.ForeignKey(User, verbose_name=_("Auteur"))
    type = models.PositiveSmallIntegerField(choices=CategorieRecette)
    difficulte = models.PositiveSmallIntegerField(choices=DifficulteRecette)
    cout = models.DecimalField(verbose_name=_("Coût"), decimal_places=2, max_digits=12,
                               validators=[MinValueValidator(Decimal('0.00'))])
    temps_preparation = models.TimeField(verbose_name=_("Temps de préparation"))
    temps_cuisson = models.TimeField(verbose_name=_("Temps de cuisson"), blank=True, null=True)
    temps_repos = models.TimeField(verbose_name=_("Temps de repos"), blank=True, null=True)
    ingredients = models.TextField(verbose_name=_("Ingrédients"))
    etape = models.TextField(verbose_name=_("Etapes"))
    note_moyenne = models.PositiveSmallIntegerField(verbose_name=_("Note obtenue"), default=0)
    photo = models.TextField(verbose_name=_("Photos"), blank=True, null=True)

    def __str__(self):
        return '[' + self.auteur.username + '] ' + self.titre + ' - ' + self.get_type_display() + ' ' \
               + self.get_difficulte_display()

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
