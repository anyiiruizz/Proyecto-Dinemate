from rest_framework import generics
from .models import Restaurante
from .serializers import RestauranteCreateSerializer, RestauranteSerializer

class RestauranteCreateView(generics.CreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteCreateSerializer

class RestauranteRetrieveView(generics.RetrieveAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteUpdateView(generics.UpdateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteDeleteView(generics.DestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteListView(generics.ListAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer