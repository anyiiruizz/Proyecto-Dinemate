from rest_framework import serializers
from .models import Usuario

class UsuarioClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','email', 'contraseña', 'nombre', 'telefono']
        extra_kwargs = {'contraseña': {'write_only': True}}

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data, tipo='cliente')