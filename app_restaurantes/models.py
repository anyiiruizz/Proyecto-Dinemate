from django.db import models
from app_usuarios.models import Usuario

class Restaurante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()

    def __str__(self):
        return self.nombre