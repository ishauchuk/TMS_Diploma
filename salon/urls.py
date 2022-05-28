from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (MastersView, PricesView, OrdersView, HomeView, AboutView,
                    PortfolioView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('masters/', MastersView.as_view(), name='masters'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
