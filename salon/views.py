from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


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


def prices(request):
    price_list = Services.objects.all()
    return render(request, 'prices.html', context={
        'title': 'Прейскурант цен и услуг',
        'price': price_list,
        'description': 'Здесь находится список услуг с ценами'
    })


def portfolio(request):
    return render(request, 'portfolio.html', context={
        'title': 'Примеры работ',
        'description': 'Здесь находятся фотографии работ наших мастеров'
    })


def orders(request):
    return render(request, 'orders.html', context={
        'title': 'Запись на услуги',
        'description': 'Здесь можно осуществить запись на услуги'
    })


def masters(request):
    masters_list = Masters.objects.all()
    return render(request, 'masters.html', context={
        'title': 'Наши мастера',
        'masters': masters_list,
        'description': 'Здесь находится информация о наших мастерах'
    })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')
