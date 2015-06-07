# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import connexion, deconnexion, inscription, Recettes, ajoutrecette, modifier, VoirRecette, commenter, \
    supprimer, voter

urlpatterns = patterns('',
                       url(r'^$', Recettes.as_view(), name='index'),
                       url(r'^index$', Recettes.as_view(), name='index'),
                       url(r'^index/(?P<type>\d+)$', Recettes.as_view(), name='index'),
                       url(r'^index/(?P<args>\w+)$', Recettes.as_view(), name='index'),
                       url(r'^connexion$', connexion, name='connexion'),
                       url(r'^deconnexion$', deconnexion, name='deconnexion'),
                       url(r'^inscription$', inscription, name='inscription'),
                       url(r'^ajouter', ajoutrecette, name='ajouter'),
                       url(r'^recette/(?P<slug>[\w-]+)$', VoirRecette.as_view(), name='recette'),
                       url(r'^modifier/(?P<slug>[\w-]+)$', modifier, name='modifier'),
                       url(r'^voter/(?P<slug>[\w-]+)$', voter, name='voter'),
                       url(r'^commenter/(?P<slug>[\w-]+)$', commenter, name='commenter'),
                       url(r'^supprimer/(?P<slug>[\w-]+)$', supprimer, name='supprimer'),
                       )
