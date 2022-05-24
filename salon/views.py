# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from .models import Services, Masters
from .forms import OrdersForm
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


def portfolio(request):
    return render(request, 'portfolio.html', context={
        'title': 'Примеры работ',
        'description': 'Здесь находятся фотографии работ наших мастеров'
    })


def orders(request):
    if request.POST:
        form = OrdersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return HttpResponse('<h1>Упс, мастер уже занят</h1>')
    return render(request, 'orders.html', {"form": OrdersForm})


class MastersView(ListView):
    model = Masters
    template_name = 'masters.html'


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')
