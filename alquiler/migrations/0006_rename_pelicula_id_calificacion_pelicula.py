# Generated by Django 5.0.4 on 2024-04-15 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alquiler', '0005_rename_cliente_id_detallealquiler_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificacion',
            old_name='pelicula_id',
            new_name='pelicula',
        ),
    ]
