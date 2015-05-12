# coding: utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from bento.forms import LoginForm, UserProfileForm
from bento.models import TypeRecette, Ingredients, DifficulteRecette, TypeRecette, Recette, Commentaires


def index(request):
    categories = TypeRecette.objects.all()
    return render(request, 'bento/index.html', {'categories-recettes' : categories})


def lire(request, id):
    try:
        recette = Recette.objects.get(id = id)
    except Recette.DoesNotExist:
        raise Http404

    return render(request, 'bento/voir.html', {'recette' : recette})


def home(request):
    text = "<h1> Bienvenue sur mon site de recette </h1>"
    return HttpResponse(text)


def view_recette(request, id_recette):
    text = "Vous avez demandé la recette n°{0}".format(id_recette)
    return HttpResponse(text)


def login(request):
    c = {}
    c.update(csrf(request))

    if len(request.GET) > 0:
        form = LoginForm(request.GET)
        if form.is_valid():
            return HttpResponseRedirect('bento/accueil.html')
    else:
        form = LoginForm()
        return render(request, 'bento/login.html', {'form' : form})

def signup(request):
    if len(request.GET) > 0:
        form = UserProfileForm(request.GET)

        if form.is_valid():
            form.save(commit = True)
            return HttpResponseRedirect('bento/login.html')
        else:
            return render_to_response('bento/login.html', {'form' : form})
    else:
        form = UserProfileForm()
        return render_to_response('bento/profil_user.html', {'form' : form})


def profil(request):
    return render(request, 'bento/profil_user.html', {})