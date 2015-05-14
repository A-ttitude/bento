# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from bento.models import Recette


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

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Confirmation du mot de passe'),
                                                                           'class': 'pure-input-1-2',
                                                                           'style': 'display: inline;'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'note_moyenne', 'photo')