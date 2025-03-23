import os
from django.db import models
from django.utils.translation import gettext_lazy as _

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='posters/')
    imdb_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        poster_path = self.poster.path if self.poster else None
        super().delete(*args, **kwargs)
        if poster_path and os.path.isfile(poster_path):
            try:
                os.remove(poster_path)
            except Exception as e:
                print(f"Error deleting file {poster_path}: {e}")