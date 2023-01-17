from django.contrib import admin

from songs.models import Singers, Albums, Songs, AlbumsSongs


@admin.register(Singers)
class SingersAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('singer', 'release_year', 'name')


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AlbumsSongs)
class AlbumsSongsAdmin(admin.ModelAdmin):
    list_display = ('album', 'seq_number', 'song')
