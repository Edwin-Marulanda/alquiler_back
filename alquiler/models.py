from django.db import models

class Cliente(models.Model):
    cedula= models.IntegerField()
    nombres= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    clave = models.CharField(max_length=150)

class Genero(models.Model):
    nombre= models.CharField(max_length=15)
    valor= models.FloatField()

class Pelicula(models.Model):
    codigo= models.IntegerField(auto_created=True, unique=True)
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=250)
    cantidad=models.IntegerField()
    genero= models.ForeignKey(Genero, on_delete=models.CASCADE)

class Calificacion(models.Model):
    puntuacion= models.IntegerField()
    comentario= models.CharField(max_length=150)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
class DetalleAlquiler(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pelicula= models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    valor= models.FloatField()
    fecha= models.DateField(null=True)
    estado = models.CharField(max_length=1,null=True)
