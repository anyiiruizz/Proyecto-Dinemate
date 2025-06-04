from django.db import models

class Usuario(models.Model):
    TIPO_CLIENTE = 'cliente'

    TIPO_CHOICES = (
        (TIPO_CLIENTE, 'Cliente'),
    #aquí para evitar su uso directo
    )

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128) 
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=TIPO_CLIENTE)

    def __str__(self):
        return self.nombre