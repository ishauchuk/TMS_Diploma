from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Домашняя страница салона-красоты.")


def about(request):
    return HttpResponse('Салон-парикмахерская "Люби Себя" рад видеть Вас.')


def prices(request):
    return HttpResponse("Здесь находится список услуг и цены.")


def portfolio(request):
    return HttpResponse("Здесь находятся примеры работ наших мастеров.")


def order(request):
    return HttpResponse("Здесь происходит запись на услуги")
