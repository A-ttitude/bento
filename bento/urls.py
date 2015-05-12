# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index, login, signup, profil

urlpatterns = patterns('',
                       url(r'^$', index, name='accueil'),
                       url(r'^login$', login, name='connexion'),
                       url(r'^signup$', signup, name='enregistrer'),
                       url(r'^profil$', profil, name='profil'),
                       )
