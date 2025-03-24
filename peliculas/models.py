from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class GeneroPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='generos_pelicula')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='peliculas_genero')

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.genero.nombre}"

