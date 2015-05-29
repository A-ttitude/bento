# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import connexion, deconnexion, inscription, Recettes, ajoutrecette, modifrecette, VoirRecette
from bento.views import supprecette

urlpatterns = patterns('',
                       url(r'^$', Recettes.as_view(), name='index'),
                       url(r'^index$', Recettes.as_view(), name='index'),
                       url(r'^connexion$', connexion, name='connexion'),
                       url(r'^deconnexion$', deconnexion, name='deconnexion'),
                       url(r'^inscription$', inscription, name='inscription'),
                       url(r'^ajoutrecette$', ajoutrecette, name='ajoutrecette'),
                       url(r'^modifrecette/(?P<pk>\d+)$', modifrecette, name='modifrecette'),
                       url(r'^recette/(?P<pk>\d+)/$', VoirRecette.as_view(), name='voirrecette'),
                       url(r'^supprecette/(?P<pk>\d+)$', supprecette, name='supprecette'),
                       )
