from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioClienteSerializer

class UsuarioClienteCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.filter(tipo='cliente')
    serializer_class = UsuarioClienteSerializer

class UsuarioClienteRetrieveView(generics.RetrieveAPIView):
    queryset = Usuario.objects.filter(tipo='cliente')
    serializer_class = UsuarioClienteSerializer

class UsuarioClienteUpdateView(generics.UpdateAPIView):
    queryset = Usuario.objects.filter(tipo='cliente')
    serializer_class = UsuarioClienteSerializer

class UsuarioClienteDeleteView(generics.DestroyAPIView):
    queryset = Usuario.objects.filter(tipo='cliente')
    serializer_class = UsuarioClienteSerializer

class UsuarioClienteListView(generics.ListAPIView):
    queryset = Usuario.objects.filter(tipo='cliente')
    serializer_class = UsuarioClienteSerializer