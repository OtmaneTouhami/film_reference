from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Film
from .forms import FilmForm

def index(request):
    films = Film.objects.all()
    return render(request, 'film/index.html', {'films': films})

def detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'film/detail.html', {'film': film})

def create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmForm()
    return render(request, 'film/create.html', {'form': form})

def update(request, film_id):
    film_id = int(film_id)
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        form = FilmForm(request.POST or None, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmForm(instance=film)
    return render(request, 'film/update.html', {'form': form})

@require_POST
def delete(request, film_id):
    film_id = int(film_id)
    try:
        film = Film.objects.get(id=film_id)
        film.delete()
    except Film.DoesNotExist:
        return redirect('index')
    return redirect('index')