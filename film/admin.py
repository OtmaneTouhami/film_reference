from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'genre')  # Columns shown in the list view
    list_filter = ('genre', 'year')  # Filter options in the sidebar
    search_fields = ('title', 'director')  # Fields that can be searched
    date_hierarchy = 'created_at'  # Adds date navigation at the top
    ordering = ('-year', 'title')  # Default sorting (newest films first, then by title)
    fields = ('title', 'director', 'year', 'description', 'genre', 'poster', 'imdb_link')  # Field order in edit form
    readonly_fields = ('created_at', 'updated_at')  # Fields that can't be edited