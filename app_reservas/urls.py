from django.urls import path
from .views import *

urlpatterns = [
    path('reservas/', ReservaListView.as_view(), name='reserva-lista'),
    path('crear/', ReservaCreateView.as_view(), name='reserva-crear'),
    path('<int:pk>/', ReservaRetrieveView.as_view(), name='reserva-detalle'),
    path('<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva-editar'),
    path('<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva-eliminar'),
]