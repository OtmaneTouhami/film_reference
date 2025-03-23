from django.urls import path
from django.conf.urls.static import static
from film_reference.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:film_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:film_id>/', views.update, name='update'),
    path('delete/<int:film_id>/', views.delete, name='delete'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
