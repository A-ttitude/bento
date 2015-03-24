# coding: utf-8

from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'bento/index.html', context)


def signup(request):
    context = {

    }
    return render(request, 'bento/signup.html', context)


def login(request):
    context = {

    }
    return render(request, 'bento/login.html', context)