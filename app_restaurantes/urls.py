from django.urls import path
from .views import (
    RestauranteCreateView, RestauranteRetrieveView,
    RestauranteUpdateView, RestauranteDeleteView,
    RestauranteListView
)

urlpatterns = [
    path('restaurantes/', RestauranteListView.as_view(), name='restaurante-lista'),
    path('crear/', RestauranteCreateView.as_view(), name='restaurante-crear'),
    path('<int:pk>/', RestauranteRetrieveView.as_view(), name='restaurante-detalle'),
    path('<int:pk>/editar/', RestauranteUpdateView.as_view(), name='restaurante-editar'),
    path('<int:pk>/eliminar/', RestauranteDeleteView.as_view(), name='restaurante-eliminar'),
]