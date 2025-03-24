from django.contrib import admin
from .models import Genero, Pelicula, GeneroPelicula

admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(GeneroPelicula)

