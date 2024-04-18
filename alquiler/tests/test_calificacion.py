from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from unittest.mock import patch
from alquiler.views import CalificacionView
from ..models import Calificacion, Pelicula, Genero

class CalificacionViewTestCase(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.url = reverse('lista_calificacion')
        self.genero = Genero.objects.create(
            nombre="nuevo genero",
            valor = 3500
        )
        self.pelicula = Pelicula.objects.create(
            codigo=40,
            nombre="nueva pelicula",
            descripcion="una pelicula de miedo",
            cantidad=3,
            genero= self.genero
        )

    def test_agregar_calificacion(self):

        response = self.cliente.post(self.url,{
                    'puntucaion' : 3,
                    'comentario' : "Muy buena...",
                    'pelicula' : self.pelicula
                    })

        print("datos "+response)
        #self.assertEqual("correcto",response.mensaje)