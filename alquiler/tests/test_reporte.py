from django.test import TestCase, Client
from django.urls import reverse, resolve
from unittest.mock import patch
from alquiler.views import ReporteView

class ReporteViewTestCase(TestCase):

    def test_get_reporte_correcto(self):
        cliente = Client()
        url = reverse('reporte_peliculas')
        response = cliente.get(url)

        print(response)