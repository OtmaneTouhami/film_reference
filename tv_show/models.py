from django.db import models
from core.models import Genre
import os


class TVShow(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    seasons = models.PositiveIntegerField()
    episodes = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='tv_posters/')
    imdb_link = models.URLField(blank=True)
    trailer_link = models.URLField(blank=True)
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