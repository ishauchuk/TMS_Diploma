from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import MastersView, PricesView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('orders/', views.orders, name='orders'),
    path('masters/', MastersView.as_view(), name='masters'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
