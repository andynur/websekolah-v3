from django.urls import path
from . import views

urlpatterns = [
    path('', views.siswa_list, name='siswa_list'),
    path('tambah/', views.siswa_create, name='siswa_create'),
    path('<int:id>/', views.siswa_detail, name='siswa_detail'),
    path('<int:id>/edit/', views.siswa_update, name='siswa_update'),
    path('<int:id>/hapus/', views.siswa_delete, name='siswa_delete'),
]