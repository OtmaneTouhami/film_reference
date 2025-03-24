from django.contrib import admin

from tv_show.models import TVShow


@admin.register(TVShow)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'start_year', 'end_year', 'seasons', 'display_genres')
    list_filter = ('genres', 'start_year')
    filter_horizontal = ('genres',)
    search_fields = ('title', 'director')
    date_hierarchy = 'created_at'
    ordering = ('-start_year', 'title')
    fields = ('title', 'director', 'start_year', 'end_year', 'seasons', 'episodes', 'description', 'genres', 'poster',
              'trailer_link', 'imdb_link', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = 'Genres'
