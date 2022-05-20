from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('price-list/', views.prices),
    path('order/', views.order),
    path('masters/', views.masters),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
