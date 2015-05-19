# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index, connexion, deconnexion, inscription, Recettes, ajoutrecette

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^index$', index, name='index'),
                       url(r'^connexion$', connexion, name='connexion'),
                       url(r'^deconnexion$', deconnexion, name='deconnexion'),
                       url(r'^inscription$', inscription, name='inscription'),
                       url(r'^recettes$', Recettes.as_view(), name='recettes'),
                       url(r'^ajoutrecette$', ajoutrecette, name='ajoutrecette'),
                       )
