from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('restaurantes/', include('restaurantes.urls')),
    path('productos/', include('productos.urls')),
    path('reservas/', include('reservas.urls')),
]
