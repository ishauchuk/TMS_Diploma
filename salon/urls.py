from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('price-list/', views.prices),
    path('order/', views.order),
]
