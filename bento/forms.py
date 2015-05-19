# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from bento.models import Recette, DifficulteRecette, CategorieRecette


class ConnexionForm(forms.Form):
    identifiant = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Identifiant'),
                                                                          'class': 'pure-input-1-2',
                                                                          'style': 'display: inline;'}))

    motpasse = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Mot de passe'),
                                                                           'class': 'pure-input-1-2',
                                                                           'style': 'display: inline;'}))


class InscriptionForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Identifiant'),
                                                                                     'class': 'pure-input-1-2',
                                                                                     'style': 'display: inline;'}))

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Prénom'),
                                                                                  'class': 'pure-input-1-2',
                                                                                  'style': 'display: inline;'}))

    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Nom'),
                                                                              'class': 'pure-input-1-2',
                                                                              'style': 'display: inline;'}))

    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email'),
                                                                             'class': 'pure-input-1-2',
                                                                             'style': 'display: inline;'}))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Mot de passe'),
                                                                            'class': 'pure-input-1-2',
                                                                            'style': 'display: inline;'}))

    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'placeholder': _('Confirmation du mot de passe'),
                                                                  'class': 'pure-input-1-2',
                                                                  'style': 'display: inline;'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RecetteForm(forms.ModelForm):
    titre = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Titre'),
                                                                    'class': 'pure-input-1-2',
                                                                    'style': 'display: inline;'}))

    auteur = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Auteur'),
                                                                     'class': 'pure-input-1-2',
                                                                     'readonly': 'readonly',
                                                                     'style': 'display: inline;'}))

    type = forms.ChoiceField(label=_('Catégorie'), choices=CategorieRecette,
                             widget=forms.Select(attrs={'placeholder': _('Catégorie'),
                                                        'class': 'pure-input-1-2',
                                                        'style': 'display: inline;'}))

    difficulte = forms.ChoiceField(label=_('Difficulté'), choices=DifficulteRecette,
                                   widget=forms.Select(attrs={'placeholder': _('Difficulté'),
                                                              'class': 'pure-input-1-2',
                                                              'style': 'display: inline'}))

    cout = forms.IntegerField(label=_('Coût'), min_value=0, initial=0,
                              widget=forms.NumberInput(attrs={'placeholder': _('Coût'),
                                                              'class': 'pure-input-1-2',
                                                              'style': 'display: inline;'}))

    temps_preparation = forms.IntegerField(label=_('Temps de préparation (minutes)'), min_value=0, initial=0,
                                           widget=forms.NumberInput(
                                               attrs={'placeholder': _('Temps de préparation (minutes)'),
                                                      'class': 'pure-input-1-2',
                                                      'style': 'display: inline;'}))

    temps_cuisson = forms.IntegerField(label=_('Temps de cuisson (minutes)'), min_value=0, initial=0,
                                       widget=forms.NumberInput(attrs={'placeholder': _('Temps de cuisson (minutes)'),
                                                                       'class': 'pure-input-1-2',
                                                                       'style': 'display: inline;'}))

    temps_repos = forms.IntegerField(label=_('Temps de repos (minutes)'), min_value=0, initial=0,
                                     widget=forms.NumberInput(attrs={'placeholder': _('Temps de repos (minutes)'),
                                                                     'class': 'pure-input-1-2',
                                                                     'style': 'display: inline;'}))

    ingredients = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Ingrédients'),
                                                                         'class': 'pure-input-1-2',
                                                                         'style': 'display: inline;'}))

    etape = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Etapes'),
                                                                   'class': 'pure-input-1-2',
                                                                   'style': 'display: inline;'}))

    photo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Photo'),
                                                                    'class': 'pure-input-1-2',
                                                                    'style': 'display: inline;'}))

    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'photo')
