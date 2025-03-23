import os
from django.db import models
from django.utils.translation import gettext_lazy as _


class Film(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'ACTION', _('Action')
        COMEDY = 'COMEDY', _('Comedy')
        DRAMA = 'DRAMA', _('Drama')
        HORROR = 'HORROR', _('Horror')
        SCIFI = 'SCIFI', _('Science Fiction')
        THRILLER = 'THRILLER', _('Thriller')
        ROMANCE = 'ROMANCE', _('Romance')
        DOCUMENTARY = 'DOCUMENTARY', _('Documentary')
        ANIMATION = 'ANIMATION', _('Animation')
        FANTASY = 'FANTASY', _('Fantasy')

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    genre = models.CharField(
        max_length=20,
        choices=Genre.choices,
        default=Genre.DRAMA,
    )
    poster = models.ImageField(
        upload_to='posters/',
    )
    imdb_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
