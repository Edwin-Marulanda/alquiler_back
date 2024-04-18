from django.db import connection

def reporte_query():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.nombre, COUNT(a.pelicula_id), SUM(a.valor) 
            FROM alquiler_detallealquiler a 
            JOIN alquiler_pelicula p ON a.pelicula_id = p.id 
            GROUP BY p.id
            ORDER BY SUM(a.valor) DESC
        """)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result_dict = {
                'id':row[0],
                'nombre': row[1],
                'num_alquilada': row[2],
                'total': row[3]
            }
            results.append(result_dict)

        return results

def pelicula_list():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT p.id, p.codigo, p.nombre, p.descripcion, p.cantidad, COALESCE(c.puntuacion, 0) AS puntuacion,
                        p.genero_id, g.nombre AS nombre_genero, g.valor AS valor_genero
                FROM alquiler_pelicula p
                LEFT JOIN 
                    (SELECT p.id, COALESCE(SUM(c.puntuacion) / COUNT(p.id), 0) AS puntuacion
                        FROM alquiler_pelicula p
                        LEFT JOIN alquiler_calificacion c ON p.id = c.pelicula_id
                        GROUP BY p.id) c ON p.id = c.id
                JOIN alquiler_genero g ON p.genero_id = g.id;
        """)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result_dict = {
                'id':row[0],
                'codigo': row[1],
                'nombre': row[2],
                'descripcion': row[3],
                'cantidad': row[4],
                'puntuacion': row[5],
                'genero': {
                    'id': row[6],
                    'nombre': row[7],
                    'valor': row[8]
                  }
            }
            results.append(result_dict)

        return results

def alquiler_cliente(pelicula_id):
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT a.id,a.valor, a.estado, a.cliente_id,a.pelicula_id,p.nombre, g.nombre,a.fecha 
                FROM alquiler_detallealquiler a JOIN alquiler_pelicula p
                ON a.pelicula_id = p.id JOIN alquiler_genero g ON p.genero_id= g.id
                where a.cliente_id = %s
                order by a.id desc
        """,[pelicula_id])
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result_dict = {
                'id':row[0],
                'valor': row[1],
                'estado':row[2],
                'cliente_id':row[3],
                'pelicula': {
                    'pelicula_id':row[4],
                    'nombre':row[5],
                    'genero':row[6]
                },
                'fecha':row[7]

            }
            results.append(result_dict)

        return results


def calificacion_pelicula(pelicula_id):
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT * 
                FROM alquiler_calificacion 
                where pelicula_id = %s
                order by puntuacion desc
        """,[pelicula_id])
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result_dict = {
                'id':row[0],
                'puntuacion': row[1],
                'comentario':row[2]
                 }

            results.append(result_dict)

        return results
