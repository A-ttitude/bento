# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index, login, signup

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^login$', login, name='login'),
                       url(r'^signup$', signup, name='signup'),
                       )
