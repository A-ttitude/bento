# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index, connexion, inscription, ajoutRecette

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^index$', index, name='index'),
                       url(r'^connexion$', connexion, name='connexion'),
                       url(r'^inscription$', inscription, name='inscription'),
                       url(r'^ajoutRecette$', ajoutRecette, name='ajoutRecette'),
                       )
