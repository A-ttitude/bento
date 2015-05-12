# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index, login, signup

urlpatterns = patterns('',
                       url(r'^$', index, name='accueil'),
                       url(r'^login$', login, name='connexion'),
                       url(r'^signup$', signup, name='enregistrer'),
                       )
