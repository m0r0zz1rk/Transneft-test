from rest_framework import viewsets, permissions

from songs.models import Singers
from songs.seializers import MusicCatalogueSerializer


class CatalogueViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр каталога исполнителей"""
    permission_classes = [permissions.AllowAny]
    queryset = Singers.objects.all()
    serializer_class = MusicCatalogueSerializer
