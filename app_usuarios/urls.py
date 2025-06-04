from django.urls import path
from .views import (
    UsuarioClienteCreateView, UsuarioClienteRetrieveView,
    UsuarioClienteUpdateView, UsuarioClienteDeleteView,
    UsuarioClienteListView
)

urlpatterns = [
    path('usuarios/', UsuarioClienteListView.as_view(), name='cliente-list'),
    path('crear/', UsuarioClienteCreateView.as_view(), name='cliente-crear'),
    path('<int:pk>/', UsuarioClienteRetrieveView.as_view(), name='cliente-detalle'),
    path('<int:pk>/editar/', UsuarioClienteUpdateView.as_view(), name='cliente-editar'),
    path('<int:pk>/eliminar/', UsuarioClienteDeleteView.as_view(), name='cliente-eliminar'),
]