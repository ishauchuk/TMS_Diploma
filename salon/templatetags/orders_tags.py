from django import template
from salon.forms import OrdersForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from salon.views import home

register = template.Library()


@register.simple_tag(name='orders')
def orders(request):

    if request.POST:
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return HttpResponseNotFound('<h1>Упс, мастер уже занят</h1>')
    return render(request, 'orders.html', {"form": OrdersForm})
