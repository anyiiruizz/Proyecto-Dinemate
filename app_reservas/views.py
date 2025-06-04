from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaCreateView(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveView(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaUpdateView(generics.UpdateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDeleteView(generics.DestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaListView(generics.ListAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer