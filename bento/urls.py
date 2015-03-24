# coding: utf-8

from django.conf.urls import patterns, url

from bento.views import index

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       )
