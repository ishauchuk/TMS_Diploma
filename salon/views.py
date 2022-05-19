from django.http import HttpResponse, HttpResponseNotFound


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


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')
