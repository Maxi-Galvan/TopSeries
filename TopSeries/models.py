from django.db import models

# Create your models here.
class serie(models.Model):
    nombre = models.TextField(max_length=100)
    temporadas = models.TextField(max_length=2)
    genero = models.TextField(max_length=15)
    descripcion = models.TextField(max_length=200)
    puntaje = models.TextField(max_length=1)
    


    def __str__(self):
        return f"{self.nombre} - {self.temporadas} - {self. descripcion}"

    
