from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Домашняя страница салона-красоты.")


def about(request):
    return HttpResponse("Мы салон-парикмахерская.")