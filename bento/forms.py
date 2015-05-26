# coding: utf-8

from decimal import Decimal

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
                                                                    'style': 'display: inline;',
                                                                    'required': 'required'}))

    auteur = forms.ModelChoiceField(label='', queryset=User.objects.all(),
                                    widget=forms.TextInput(attrs={'readonly': 'readonly',
                                                                  'style': 'display: none;'}))

    type = forms.ChoiceField(label=_('Catégorie'), choices=CategorieRecette,
                             widget=forms.Select(attrs={'placeholder': _('Catégorie'),
                                                        'class': 'pure-input-1-2',
                                                        'style': 'display: inline;',
                                                        'required': 'required'}))

    difficulte = forms.ChoiceField(label=_('Difficulté'), choices=DifficulteRecette,
                                   widget=forms.Select(attrs={'placeholder': _('Difficulté'),
                                                              'class': 'pure-input-1-2',
                                                              'style': 'display: inline',
                                                              'required': 'required'}))

    cout = forms.DecimalField(label=_('Coût'), decimal_places=2, max_digits=12, min_value=Decimal('0.00'), initial=0.00,
                              widget=forms.NumberInput(attrs={'placeholder': _('Coût'),
                                                              'class': 'pure-input-1-2',
                                                              'style': 'display: inline;',
                                                              'required': 'required'}))

    temps_preparation = forms.TimeField(label=_('Temps de préparation (hh:mm)'),
                                        widget=forms.TimeInput(format='%H:%M',
                                                               attrs={'placeholder': _('Temps de préparation (hh:mm)'),
                                                                      'class': 'pure-input-1-2',
                                                                      'style': 'display: inline;',
                                                                      'required': 'required'}))

    temps_cuisson = forms.TimeField(label=_('Temps de cuisson (hh:mm)'),
                                    widget=forms.TimeInput(format='%H:%M',
                                                           attrs={'placeholder': _('Temps de cuisson (hh:mm)'),
                                                                  'class': 'pure-input-1-2',
                                                                  'style': 'display: inline;'}))

    temps_repos = forms.TimeField(label=_('Temps de repos (hh:mm)'),
                                  widget=forms.TimeInput(format='%H:%M',
                                                         attrs={'placeholder': _('Temps de repos (hh:mm)'),
                                                                'class': 'pure-input-1-2',
                                                                'style': 'display: inline;'}))

    ingredients = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Ingrédients'),
                                                                         'class': 'pure-input-1-2',
                                                                         'style': 'display: inline;',
                                                                         'required': 'required'}))

    etape = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Etapes'),
                                                                   'class': 'pure-input-1-2',
                                                                   'style': 'display: inline;',
                                                                   'required': 'required'}))

    photo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Photo'),
                                                                    'class': 'pure-input-1-2',
                                                                    'style': 'display: inline;'}))

    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'photo')
