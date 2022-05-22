# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Services, Masters
from .forms import *
from django.views.generic import ListView


def home(request):
    return render(request, 'home_page.html', context={
        'title': 'Домашняя',
        'description': 'Сайт салона-парикмехерской "Люби-себя"'
    })


def about(request):
    return render(request, 'about.html', context={
        'title': 'О нас',
        'description': 'Контактный номер телефона/Адрес'
    })


class PricesView(ListView):
    model = Services
    template_name = 'prices.html'
    extra_context = {'title': 'Прейскурант цен и услуг',
        'description': 'Здесь находится список услуг с ценами'}

# class PortfolioView(ListView):
#     # model = Services
#     template_name = 'prices.html'
#     extra_context = {'title': 'Примеры работ',
#         'description': 'Здесь находятся фотографии работ наших мастеров'}


def portfolio(request):
    return render(request, 'portfolio.html', context={
        'title': 'Примеры работ',
        'description': 'Здесь находятся фотографии работ наших мастеров'
    })


def orders(request):
    # form = TestForm()
    return render(request, 'orders.html', context={
        'title': 'Запись на услуги',
        # 'form': form,
        'description': 'Здесь можно осуществить запись на услуги'
    })


class MastersView(ListView):
    model = Masters
    template_name = 'masters.html'

# def masters(request):
#     return render(request, 'masters.html', context={
#         'title': 'Наши мастера',
#         'description': 'Здесь находится информация о наших мастерах'
#     })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')


def addclient(request):
    if request.POST:
        form = AddClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request, 'addorder.html', {"form": AddClient})


def login(request):
    return render(request, 'login.html', context={
        'title': 'Авторизация',
        'description': 'Сайт салона-парикмехерской "Люби-себя"'
    })