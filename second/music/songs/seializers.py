from rest_framework import serializers

from songs.models import Singers, Albums, Songs, AlbumsSongs


class AlbumsSongsSerializer(serializers.ModelSerializer):
    """Сериализация данных модели песен в альбомах"""
    song_name = serializers.SerializerMethodField()

    class Meta:
        model = AlbumsSongs
        fields = ('seq_number', 'song_name')

    def get_song_name(self, obj):
        return Songs.objects.get(id=obj.song_id).name


class AlbumsSerializer(serializers.ModelSerializer):
    """Сериализация данных модели альбомов"""
    albumsongs = serializers.SerializerMethodField()

    class Meta:
        model = Albums
        fields = ('name', 'release_year', 'albumsongs')

    def get_albumsongs(self, obj):
        ordered_queryset = AlbumsSongs.objects.filter(album_id=obj.id).order_by('seq_number')
        return AlbumsSongsSerializer(ordered_queryset, many=True, context=self.context).data


class MusicCatalogueSerializer(serializers.ModelSerializer):
    """Сериализация каталога исполнителей и их альбомов с песнями"""
    albums = AlbumsSerializer(
        many=True
    )

    class Meta:
        model = Singers
        fields = ('name', 'albums')