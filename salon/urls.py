from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('prices/', views.prices),
    path('orders/', views.orders),
    path('masters/', views.masters),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
