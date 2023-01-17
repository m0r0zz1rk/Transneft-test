from django.urls import path

from songs.api_views import CatalogueViewSet

urlpatterns = [
    path('catalogue/', CatalogueViewSet.as_view({'get': 'list'}))
]