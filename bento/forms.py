# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from bento.models import Recette


class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email'),
                                                                     'class': 'pure-input-1-2',
                                                                     'style': 'display: inline;'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Mot de passe'),
                                                                           'class': 'pure-input-1-2',
                                                                           'style': 'display: inline;'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            result = User.objects.filter(password=password, email=email)
            if len(result) != 1:
                raise forms.ValidationError(_('Email ou mot de passe invalide !'))

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Pseudo'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Prénom'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Nom'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Mot de passe'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class RecetteForm(forms.ModelForm):
    titre = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Titre'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    auteur = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Auteur'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    type = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Catégorie'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    difficulte = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Difficulté'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    cout = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Coût'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    temps_preparation = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Temps de préparation'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    temps_cuisson = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Temps de cuisson'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    temps_repos = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Temps de repos'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    ingredients = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Ingrédients'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    etape = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': _('Etapes'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))
    photo = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Photo'), 'class': 'pure-input-1-2', 'style': 'display: inline;'}))

    class Meta:
        model = Recette
        fields = ('titre', 'auteur', 'type', 'difficulte', 'cout', 'temps_preparation', 'temps_cuisson', 'temps_repos',
                  'ingredients', 'etape', 'photo')