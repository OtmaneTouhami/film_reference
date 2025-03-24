from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from .models import Film
from .forms import FilmForm

@login_required
def index(request):
    search_query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'title')

    films = Film.objects.all().order_by('-year')

    if search_query:
        if search_type == 'title':
            films = films.filter(title__icontains=search_query)
        elif search_type == 'director':
            films = films.filter(director__icontains=search_query)
        elif search_type == 'year':
            try:
                year = int(search_query)
                films = films.filter(year=year)
            except ValueError:
                pass

    paginator = Paginator(films, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'film/index.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'search_type': search_type
    })

@login_required
def detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'film/detail.html', {'film': film})

@login_required
def create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmForm()
    return render(request, 'film/create.html', {'form': form})

@login_required
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

@login_required
@require_POST
def delete(request, film_id):
    film_id = int(film_id)
    try:
        film = Film.objects.get(id=film_id)
        film.delete()
    except Film.DoesNotExist:
        return redirect('index')
    return redirect('index')