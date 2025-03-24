from rest_framework import serializers
from .models import Pelicula, Genero, GeneroPelicula

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'   
        #fields = ['id', 'nombre']

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'   
        #fields = ['id', 'titulo', 'descripcion']

class GeneroPeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroPelicula
        fields = '__all__'   
