from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from .models import TVShow
from .forms import TvShowForm

@login_required
def index(request):
    search_query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'title')

    tv_shows = TVShow.objects.all().order_by('-start_year')

    if search_query:
        if search_type == 'title':
            tv_shows = tv_shows.filter(title__icontains=search_query)
        elif search_type == 'director':
            tv_shows = tv_shows.filter(director__icontains=search_query)
        elif search_type == 'start_year':
            try:
                start_year = int(search_query)
                tv_shows = tv_shows.filter(start_year=start_year)
            except ValueError:
                pass

    paginator = Paginator(tv_shows, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'show/index.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'search_type': search_type
    })

@login_required
def detail(request, show_id):
    tv_show = TVShow.objects.get(id=show_id)
    return render(request, 'show/detail.html', {'tv_show': tv_show})

@login_required
def create(request):
    if request.method == 'POST':
        form = TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tv_show_index')
    else:
        form = TvShowForm()
    return render(request, 'show/create.html', {'form': form})

@login_required
def update(request, show_id):
    show_id = int(show_id)
    try:
        tv_show = TVShow.objects.get(id=show_id)
    except TVShow.DoesNotExist:
        return redirect('tv_show_index')

    if request.method == 'POST':
        form = TvShowForm(request.POST, request.FILES, instance=tv_show)
        if form.is_valid():
            form.save()
            return redirect('tv_show_index')
    else:
        form = TvShowForm(instance=tv_show)
    return render(request, 'show/update.html', {'form': form})

@login_required
@require_POST
def delete(request, show_id):
    show_id = int(show_id)
    try:
        tv_show = TVShow.objects.get(id=show_id)
        tv_show.delete()
    except TVShow.DoesNotExist:
        return redirect('tv_show_index')
    return redirect('tv_show_index')
