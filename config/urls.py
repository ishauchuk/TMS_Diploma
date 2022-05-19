from django.contrib import admin
from django.urls import path, include
from salon.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('salon.urls')),
]

handler404 = pageNotFound
