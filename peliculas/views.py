from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pelicula, Genero, GeneroPelicula
from .serializers import PeliculaSerializer, GeneroSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all().prefetch_related('generos_pelicula__genero')
    serializer_class = PeliculaSerializer

    @action(detail=False, methods=['get'], url_path='buscar-por-titulo')
    def buscar(self, request):
        titulo = request.query_params.get('titulo', '')
        if not titulo:
            return Response({"error": "Debes enviar el parámetro 'titulo'."}, status=400)
        peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
        serializer = self.get_serializer(peliculas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='generos')
    def generos(self, request, pk=None):
        pelicula = self.get_object()
        generos = GeneroPelicula.objects.filter(pelicula=pelicula).values_list('genero__nombre', flat=True)
        return Response({"generos": list(generos)})


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().prefetch_related('peliculas_genero__pelicula')
    serializer_class = GeneroSerializer

    @action(detail=True, methods=['get'], url_path='peliculas')
    def peliculas(self, request, pk=None):
        genero = self.get_object()
        peliculas = GeneroPelicula.objects.filter(genero=genero).select_related('pelicula')
        serializer = PeliculaSerializer([gp.pelicula for gp in peliculas], many=True)
        return Response(serializer.data)

