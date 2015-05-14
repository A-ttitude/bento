# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bento.forms import ConnexionForm, InscriptionForm, RecetteForm
from bento.models import TypeRecette, Recette


def index(request):
    categories = TypeRecette.objects.all()
    return render(request, 'bento/index.html', {'categories-recettes': categories})


def lire(request, _id):
    try:
        recette = Recette.objects.get(id=_id)
    except Recette.DoesNotExist:
        raise Http404

    return render(request, 'bento/voir.html', {'recette': recette})


def view_recette(request, id_recette):
    text = _("Vous avez demandé la recette n°{0}").format(id_recette)
    return HttpResponse(text)


@login_required
def deconnexion(request):
    logout(request)
    return render(request, 'bento/index.html')


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
                    return render(request, 'bento/index.html')
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
            return render(request, 'bento/connexion.html')
    else:
        formulaire = InscriptionForm()

    return render(request, 'bento/inscription.html', {'formulaire': formulaire})


@login_required
def ajoutrecette(request):
    if request.method == 'POST':
        formulaire = RecetteForm(request.POST)

        if formulaire.is_valid():
            formulaire.save(commit=True)
            return render(request, 'bento/index.html')
        else:
            return render(request, 'bento/recette.html', {'formulaire': formulaire})
    else:
        formulaire = RecetteForm()

    return render(request, 'bento/recette.html', {'formulaire': formulaire})