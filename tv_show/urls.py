from django.urls import path
from django.conf.urls.static import static
from film_reference.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.index, name='tv_show_index'),
    path('detail/<int:show_id>/', views.detail, name='tv_show_detail'),
    path('create/', views.create, name='tv_show_create'),
    path('update/<int:show_id>/', views.update, name='tv_show_update'),
    path('delete/<int:show_id>/', views.delete, name='tv_show_delete'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
