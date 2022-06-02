# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Services, Masters, Orders
from .forms import OrdersForm
from django.views.generic import ListView, CreateView, View


class HomeView(View):
    template_name = 'home_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'title': 'Домашняя',
        })


class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'title': 'О нас',
            'description': 'О нас',
        })


class PricesView(ListView):
    model = Services
    template_name = 'prices.html'
    extra_context = {'title': 'Прейскурант цен и услуг',
                     'description': 'Прейскурант услуг и цен', }


class PortfolioView(View):
    template_name = 'portfolio.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'title': 'Примеры работ',
            'description': 'Фотографии работ наших мастеров',
        })


class OrdersView(CreateView):
    model = Orders
    template_name = 'orders.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'orders.html', {"form": OrdersForm})

    def post(self, request, *args, **kwargs):
        form = OrdersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        return render(request, self.template_name, {'form': form})


class MastersView(ListView):
    model = Masters
    template_name = 'masters.html'
    extra_context = {'title': 'Наши мастера',
                     'description': 'Наши мастера', }


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, такой страницы нет</h1>')
