from rest_framework import serializers
from app_usuarios.models import Usuario
from .models import Restaurante

class UsuarioRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','email', 'contraseña', 'nombre', 'telefono']
        extra_kwargs = {'contraseña': {'write_only': True}}

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data, tipo='restaurante')

class RestauranteCreateSerializer(serializers.ModelSerializer):
    usuario = UsuarioRestauranteSerializer()

    class Meta:
        model = Restaurante
        fields = ['id','usuario', 'nombre', 'categoria', 'direccion', 'telefono', 'correo', 'hora_apertura', 'hora_cierre']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UsuarioRestauranteSerializer.create(UsuarioRestauranteSerializer(), validated_data=usuario_data)
        restaurante = Restaurante.objects.create(usuario=usuario, **validated_data)
        return restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id', 'usuario', 'nombre', 'categoria', 'direccion', 'telefono', 'correo', 'hora_apertura', 'hora_cierre']