from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(DetalleAlquiler)

