"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from api.views import ServicesAPIView, MastersAPIView, ClientsAPIView, \
    OrdersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/services', ServicesAPIView.as_view()),
    path('api/v1/masters', MastersAPIView.as_view()),
    path('api/v1/clients', ClientsAPIView.as_view()),
    path('api/v1/clients/<int:id>', ClientsAPIView.as_view()),
    path('api/v1/orders', OrdersAPIView.as_view()),
    # path('api/v1/'),
]

# urlpatterns += static(static(settings.MEDIA_URL, document_roo=settings.MEDIA_ROOT))
