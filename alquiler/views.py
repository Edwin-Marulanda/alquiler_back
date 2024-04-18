import json
import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .customquery import reporte_query, pelicula_list,alquiler_cliente, calificacion_pelicula

from .models import Pelicula, Cliente, DetalleAlquiler, Calificacion, Genero

class PeliculaView(View):
    #permiso acceso
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args,**kwargs)

    def get(self,request,id=0):
        if id>0:
            peliculas = list(Pelicula.objects.filter(id=id).values())

            if len(peliculas)>0:
                pelicula = peliculas[0]
                datos = {'mensaje': 'correcto', 'pelicula': pelicula}
            else:
                datos = {'mensaje': 'No se encontro la pelicula'}
            return JsonResponse(datos)
        else:

            peliculas = list(pelicula_list())

            if len(peliculas)>0:
                datos = {'mensaje': 'correcto', 'peliculas': peliculas}
            else:
                datos = {'mensaje': 'No se encontraron peliculas'}

            return JsonResponse(datos)

    def post(self, request):
        jsonData = json.loads(request.body)
        Pelicula.objects.create(
            codigo = jsonData['codigo'],
            nombre = jsonData['nombre'],
            descripcion = jsonData['descripcion'],
            cantidad = jsonData['cantidad'],
            genero = jsonData['genero']
        )
        datos = {'mensaje':'Inserción exitosa'}
        return JsonResponse(datos)

    def put(self, request,id):
        #jsonData  =  json.loads(request.body)
        peliculas = list(Pelicula.objects.filter(id=id).values())
        if len(peliculas)>0:
            pelicula = Pelicula.objects.get(id=id)
            pelicula.cantidad +=1
            pelicula.save()
            datos = {'mensaje': 'actualizacion correcta'}
        else:
            datos = {'mensaje': 'actualizacion fallida'}

        return JsonResponse(datos)

    def delete(self, request):
        pass

class ClienteView(View):

    #permiso acceso
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args,**kwargs)

    def get(self,request,cedula=0):
        if cedula>0:
            clientes = list(Cliente.objects.filter(cedula=cedula).values())

            if len(clientes)>0:
                cliente = clientes[0]
                datos = {'mensaje': 'correcto', 'cliente': cliente}
            else:
                datos = {'mensaje': 'No se encontro la cliente'}
            return JsonResponse(datos)
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes)>0:
                datos = {'mensaje': 'correcto', 'clientes': clientes}
            else:
                datos = {'mensaje': 'No se encontraron clientes'}

            return JsonResponse(datos)

    def post(self, request):
        jsonData = json.loads(request.body)
        Pelicula.objects.create(
            codigo = jsonData['codigo'],
            nombre = jsonData['nombre'],
            descripcion = jsonData['descripcion'],
            cantidad = jsonData['cantidad'],
            genero = jsonData['genero']
        )
        datos = {'mensaje':'Inserción exitosa'}
        return JsonResponse(datos)

    def put(self, request):
        pass
    def delete(self, request):
        pass


class DetalleAlquilerView(View):

    #permiso acceso
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args,**kwargs)

    def get(self,request,id=0):
        if id>0:
            detallesAlquiler = list(alquiler_cliente(id))

            if len(detallesAlquiler)>0:
                datos = {'mensaje': 'correcto', 'detalles_alquiler': detallesAlquiler}
            else:
                datos = {'mensaje': 'No se encontraron detalles de alquiler'}
            return JsonResponse(datos)

    def post(self, request):
        jsonData = json.loads(request.body)
        cliente_id = jsonData['cliente']
        cliente = get_object_or_404(Cliente, id=cliente_id)
        pelicula_id = jsonData['pelicula']
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)

        DetalleAlquiler.objects.create(
            cliente = cliente,
            pelicula= pelicula,
            valor = jsonData['valor'],
            estado = jsonData['estado'],
            fecha= datetime.date.today()
        )
        datos = {'mensaje':'Inserción exitosa'}
        return JsonResponse(datos)

    def put(self, request,id):
        detallesAlquiler = list(DetalleAlquiler.objects.filter(id=id).values())
        if len(detallesAlquiler)>0:
            detallesAlquiler = DetalleAlquiler.objects.get(id=id)
            detallesAlquiler.estado= "E"
            detallesAlquiler.save()
            datos = {'mensaje': 'actualizacion correcta'}
        else:
            datos = {'mensaje': 'actualizacion fallida'}

        return JsonResponse(datos)

    def delete(self, request):
        pass


class CalificacionView(View):
    #permiso acceso
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args,**kwargs)

    def get(self,request,id=0):
        if id>0:
            calificaciones = list(calificacion_pelicula(id))

            if len(calificaciones)>0:
                datos = {'mensaje': 'correcto', 'calificaciones': calificaciones}
            else:
                datos = {'mensaje': 'No se encontraron calificaciones'}
            return JsonResponse(datos)

    def post(self, request):
        jsonData = json.loads(request.body)

        pelicula_id = jsonData['pelicula']
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)

        Calificacion.objects.create(
            puntuacion=jsonData['puntuacion'],
            comentario= jsonData['comentario'],
            pelicula = pelicula
        )
        datos = {'mensaje':'Inserción exitosa'}
        return JsonResponse(datos)

    def put(self, request,id):
        pass
    def delete(self, request):
        pass

class GeneroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            generos = list(Genero.objects.filter(id=id).values())

            if len(generos)>0:
                genero = generos[0]
                datos = {'mensaje': 'correcto', 'genero': genero}
            else:
                datos = {'mensaje': 'No se encontro el genero'}
            return JsonResponse(datos)
        else:

            generos = list(Genero.objects.values())

            if len(generos)>0:
                datos = {'mensaje': 'correcto', 'generos': generos}
            else:
                datos = {'mensaje': 'No se encontraron generos'}

            return JsonResponse(datos)

    def put(self, request, id):
            jsonData = json.loads(request.body)
            genero = list(Genero.objects.filter(id=id).values())

            if len(genero) > 0:
                genero = Genero.objects.get(id=id)
                genero.valor = jsonData['valor']
                genero.save()

                datos = {'mensaje': 'actualizacion correcta'}
            else:
                datos = {'mensaje': 'actualizacion fallida'}

            return JsonResponse(datos)


class ReporteView(View):
    # permiso acceso
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        reporte = list(reporte_query())
        if len(reporte) > 0:
           datos = {'mensaje': 'correcto', 'reporte': reporte}
        else:
           datos = {'mensaje': 'No se genero el reporte'}

        return JsonResponse(datos)
