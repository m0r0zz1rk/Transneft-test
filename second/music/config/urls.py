from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/songs/', include('songs.api_urls'))
]

urlpatterns += docs_urls
