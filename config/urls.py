# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crud.urls')),  # Incluye las rutas de la app CRUD
]
