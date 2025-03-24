from django import forms
from .models import TVShow
from core.models import Genre
from datetime import date


class TvShowForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = TVShow
        fields = ['title', 'director', 'start_year', 'end_year', 'seasons', 'episodes', 'description', 'genres',
                  'poster','trailer_link', 'imdb_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_year': forms.NumberInput(attrs={'min': 1888, 'max': date.today().year + 1}),
            'end_year': forms.NumberInput(attrs={'min': 1888, 'max': date.today().year + 1}),
            'seasons': forms.NumberInput(attrs={'min': 1}),
            'episodes': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genres'].widget.attrs.update({'class': 'flex flex-wrap gap-4'})
        for field in self.fields:
            if field != 'genres':
                self.fields[field].widget.attrs.update({
                    'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
                })
        self.fields['poster'].widget.attrs.update({
            'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
        })

    def clean_start_year(self):
        start_year = self.cleaned_data.get('start_year')
        if start_year < 1888 or start_year > date.today().year + 1:
            raise forms.ValidationError(f"Start year must be between 1888 and {date.today().year + 1}")
        return start_year
