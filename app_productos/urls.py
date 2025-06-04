from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-lista'),
    path('crear/', ProductoCreateView.as_view(), name='producto-crear'),
    path('<int:pk>/', ProductoRetrieveView.as_view(), name='producto-detalle'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-editar'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-eliminar'),
]