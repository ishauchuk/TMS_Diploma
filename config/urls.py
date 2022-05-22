from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from salon.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('salon.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
