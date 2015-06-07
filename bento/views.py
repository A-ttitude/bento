# coding: utf-8

from django.views.generic import ListView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q

from bento.forms import ConnexionForm, InscriptionForm, RecetteForm, CommentaireForm
from bento.models import Recette, Commentaires, Vote


# Class

class Recettes(ListView):
    model = Recette
    template_name = 'bento/index.html'

    def get_queryset(self):
        try:
            type_recette = self.kwargs['type']
        except KeyError:
            type_recette = ''

        try:
            args = self.kwargs['args']
        except KeyError:
            args = ''

        if type_recette != '':
            object_list = self.model.objects.filter(type=type_recette)
        elif args != '':
            object_list = self.model.objects.filter(Q(titre__contains=args) | Q(ingredients__contains=args))
        else:
            object_list = self.model.objects.all()

        return object_list.order_by('note_moyenne').reverse()


class VoirRecette(DetailView):
    model = Recette
    template_name = 'bento/une_recette.html'

    def get(self, request, *args, **kwargs):
        try:
            setattr(self, 'object', self.get_object())
            setattr(request, 'commentaires', Commentaires.objects.filter(recette=self.get_object()))
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
            formulaire.save()
            return redirect('/connexion')
    else:
        formulaire = InscriptionForm()

    return render(request, 'bento/inscription.html', {'formulaire': formulaire})


@login_required
def ajoutrecette(request):
    if request.method == 'POST':
        formulaire = RecetteForm(request.POST, initial={'auteur': request.user})

        if formulaire.is_valid():
            formulaire.save()
            return redirect('/index')
        else:
            return render(request, 'bento/ajoutrecette.html', {'formulaire': formulaire})
    else:
        formulaire = RecetteForm(initial={'auteur': request.user})

    return render(request, 'bento/ajoutrecette.html', {'formulaire': formulaire})


@login_required
def modifier(request, slug):
    try:
        recette = Recette.objects.get(slug=slug)

        if request.user == recette.auteur:
            if request.method == 'POST':
                formulaire = RecetteForm(request.POST, instance=recette)
                if formulaire.is_valid():
                    formulaire.save()
            else:
                if slug:
                    formulaire = RecetteForm(instance=recette)
                    return render(request, 'bento/modifrecette.html',
                                  {'slug': slug, 'formulaire': formulaire})
        else:
            messages.error(request, _('Vous n\'êtes pas l\'auteur de cette recette.'))

    except Recette.DoesNotExist:
        messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')


@login_required
def supprimer(request, slug):
    if slug:
        try:
            recette = Recette.objects.get(slug=slug)

            if request.user == recette.auteur:
                recette.delete()
            else:
                messages.error(request, _('Vous n\'êtes pas l\'auteur de cette recette.'))
        except Recette.DoesNotExist:
            messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')


@login_required
def commenter(request, slug):
    try:
        recette = Recette.objects.get(slug=slug)

        if request.method == 'POST':
            formulaire = CommentaireForm(request.POST, initial={'auteur': request.user, 'recette': recette})
            if formulaire.is_valid():
                formulaire.save()
        else:
            if slug:
                formulaire = CommentaireForm(initial={'auteur': request.user, 'recette': recette})
                return render(request, 'bento/commentairerecette.html',
                              {'slug': slug, 'formulaire': formulaire})

        return redirect('/recette/' + slug)

    except Recette.DoesNotExist:
        messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')


@login_required
def voter(request, slug):
    try:
        recette = Recette.objects.get(slug=slug)

        if not Vote.objects.filter(utilisateur=request.user, recette=recette):
            vote = Vote(utilisateur=request.user, recette=recette)
            vote.save()
            recette.note_moyenne += 1
            recette.save()
        else:
            messages.error(request, _('Vous avez déjà voté pour cette recette !'))

        return redirect('/recette/' + slug)

    except Recette.DoesNotExist:
        messages.error(request, _('Cette recette n\'existe pas.'))

    return redirect('/index')
