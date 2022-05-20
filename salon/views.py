from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html', context={
        'title': 'Домашняя',
        'description': 'Сайт салона-парикмехерской "Люби-себя"'
    })


def about(request):
    return render(request, 'home_page.html', context={
        'title': 'О нас',
        'description': 'Контактный номер телефона/Адрес'
    })


def prices(request):
    return render(request, 'home_page.html', context={
        'title': 'Прейскурант цен и услуг',
        'description': 'Здесь находится список услуг с ценами'
    })


def portfolio(request):
    return render(request, 'home_page.html', context={
        'title': 'Примеры работ',
        'description': 'Здесь находятся фотографии работ наших мастеров'
    })


def order(request):
    return render(request, 'home_page.html', context={
        'title': 'Запись на услуги',
        'description': 'Здесь можно осуществить запись на услуги'
    })


def masters(request):
    return render(request, 'home_page.html', context={
        'title': 'Наши мастера',
        'description': 'Здесь находится информация о наших мастерах'
    })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')
