from django.contrib import admin
from .models import Film, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'display_genres')
    list_filter = ('genres', 'year')
    filter_horizontal = ('genres',)
    search_fields = ('title', 'director')
    date_hierarchy = 'created_at'
    ordering = ('-year', 'title')
    fields = ('title', 'director', 'year', 'description', 'genres', 'poster', 'imdb_link', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = 'Genres'