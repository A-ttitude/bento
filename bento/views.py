# coding: utf-8

from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bento.forms import ConnexionForm, InscriptionForm, RecetteForm
from bento.models import Recette


# Class

class Recettes(generic.ListView):
    model = Recette
    template_name = 'bento/index.html'


class VoirRecette(generic.DetailView):
    model = Recette
    template_name = 'bento/une_recette.html'


# Def

def deconnexion(request):
    logout(request)
    return redirect('/index')


# Formulaires

def connexion(request):
    if request.method == 'POST':
        formulaire = ConnexionForm(request.POST)

        if formulaire.is_valid():
            user = authenticate(username=formulaire.cleaned_data['identifiant'],
                                password=formulaire.cleaned_data['motpasse'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/index')
                else:
                    messages.error(request, _('Votre compte est désactivé.'))
            else:
                messages.error(request, _('Vos identifiants sont invalides.'))
    else:
        formulaire = ConnexionForm()

    return render(request, 'bento/connexion.html', {'formulaire': formulaire})


def inscription(request):
    if request.method == 'POST':
        formulaire = InscriptionForm(request.POST)

        if formulaire.is_valid():
            formulaire.save(commit=True)
            return redirect('/connexion')
    else:
        formulaire = InscriptionForm()

    return render(request, 'bento/inscription.html', {'formulaire': formulaire})


@login_required
def ajoutrecette(request):
    if request.method == 'POST':
        formulaire = RecetteForm(request.POST, initial={'auteur': request.user})

        if formulaire.is_valid():
            formulaire.save(commit=True)
            return redirect('/index')
        else:
            return render(request, 'bento/ajoutrecette.html', {'formulaire': formulaire})
    else:
        formulaire = RecetteForm(initial={'auteur': request.user})

    return render(request, 'bento/ajoutrecette.html', {'formulaire': formulaire})


@login_required
def modifrecette(request, id_recette):
    if id_recette:
        if len(request.GET) > 0:
            # if form.is_valid():
            pass
