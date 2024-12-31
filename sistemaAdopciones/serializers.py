from rest_framework import serializers
from .models import Animal, Usuario, SolicitudAdopcion
from django.contrib.auth.hashers import make_password
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'telefono', 'direccion', 'tipo_usuario']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Usuario.objects.create(**validated_data)

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__' 

class SolicitudAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAdopcion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'