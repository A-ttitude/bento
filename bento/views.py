# coding: utf-8

from django.views.generic import ListView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from bento.forms import ConnexionForm, InscriptionForm, RecetteForm
from bento.models import Recette


# Class

class Recettes(ListView):
    model = Recette
    template_name = 'bento/index.html'


class VoirRecette(DetailView):
    model = Recette
    template_name = 'bento/une_recette.html'

    def get(self, request, *args, **kwargs):
        try:
            setattr(self, 'object', self.get_object())
        except Http404:
            messages.error(request, _('Cette recette n\'existe pas.'))
            return redirect('/index')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


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
    try:
        recette = Recette.objects.get(pk=id_recette)

        if request.user == recette.auteur:
            if request.method == 'POST':
                formulaire = RecetteForm(request.POST, instance=recette)
                if formulaire.is_valid():
                    formulaire.save(commit=True)
            else:
                if id_recette:
                    formulaire = RecetteForm(instance=recette)
                    return render(request, 'bento/modifrecette.html', {'id_recette': id_recette, 'formulaire': formulaire})
        else:
            messages.error(request, _('Vous n\'êtes pas l\'auteur de cette recette.'))

    except Recette.DoesNotExist:
        messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')


@login_required
def supprecette(request, id_recette):
    if id_recette:
        try:
            recette = Recette.objects.get(pk=id_recette)

            if request.user == recette.auteur:
                recette.delete()
            else:
                messages.error(request, _('Vous n\'êtes pas l\'auteur de cette recette.'))
        except Recette.DoesNotExist:
            messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')
