from django.urls import path
from .views import PeliculaView, ReporteView, DetalleAlquilerView,ClienteView,CalificacionView,GeneroView

urlpatterns = [
    path('peliculas/',PeliculaView.as_view(), name='lista_peliculas'),
    path('peliculas/<int:id>', PeliculaView.as_view(), name='gestion_peliculas'),
    path('clientes/', ClienteView.as_view(), name='lista_clientes'),
    path('clientes/<int:cedula>', ClienteView.as_view(), name='gestion_clientes'),
    path('reporte/',ReporteView.as_view(), name='reporte_peliculas'),
    path('alquiler/',DetalleAlquilerView.as_view(), name='detalle_alquiler'),
    path('alquiler/<int:id>',DetalleAlquilerView.as_view(), name='gestion_alquiler'),
    path('calificacion/',CalificacionView.as_view(),name='lista_calificacion'),
    path('calificacion/<int:id>',CalificacionView.as_view(),name='gestion_calificacion'),
    path('genero/', GeneroView.as_view(), name='listar-generos'),
    path('genero/<int:id>', GeneroView.as_view(), name='gestion-generos')
]