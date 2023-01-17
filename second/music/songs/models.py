from django.core.validators import MinValueValidator
from django.db import models


class Singers(models.Model):
    """Модель исполнителей"""
    name = models.CharField(
        max_length=200,
        blank=False,
        unique=True,
        verbose_name='Название/Имя'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Albums(models.Model):
    """Модель альбомов"""
    singer = models.ForeignKey(
        Singers,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        verbose_name='Исполнитель',
        related_name="albums"
    )
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1800), ],
        blank=True,
        default=2000,
        verbose_name='Год выпуска'
    )
    name = models.CharField(
        max_length=200,
        blank=False,
        default='Альбом',
        verbose_name='Название альбома'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} ("{self.singer.name}", {str(self.release_year)} г.)'

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Songs(models.Model):
    """Модель песен"""
    name = models.CharField(
        max_length=200,
        blank=False,
        default='Песня',
        verbose_name='Название песни'
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class AlbumsSongs(models.Model):
    """Модель песен в альбомах"""
    album = models.ForeignKey(
        Albums,
        on_delete=models.CASCADE,
        verbose_name='Альбом',
        related_name='albumsongs'
    )
    seq_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1), ],
        default=1,
        verbose_name='Порядковый номер песни в альбоме'
    )
    song = models.ForeignKey(
        Songs,
        on_delete=models.CASCADE,
        verbose_name='Песня'
    )

    objects = models.Manager()

    def __str__(self):
        return f'Альбом "{self.album.name}": песня "{self.song.name}"'

    class Meta:
        verbose_name = 'Песня в альбоме'
        verbose_name_plural = 'Песни в альбомах'
        unique_together = ('album', 'seq_number')
