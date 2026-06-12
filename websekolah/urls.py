from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # always redirect to /siswa
    path('', lambda request: redirect('siswa_list')),
    path('admin/', admin.site.urls),
    path('siswa/', include('siswa.urls')),
]