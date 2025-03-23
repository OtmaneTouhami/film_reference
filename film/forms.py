from django import forms
from .models import Film, Genre

class FilmForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Film
        fields = ['title', 'director', 'year', 'description', 'genres', 'poster', 'imdb_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'year': forms.NumberInput(attrs={'min': 1888, 'max': 2100}),
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

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1888 or year > 2100:
            raise forms.ValidationError("Year must be between 1888 and 2100")
        return year