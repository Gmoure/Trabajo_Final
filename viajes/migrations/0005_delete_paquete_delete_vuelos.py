# Generated by Django 4.1.2 on 2022-11-05 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0004_rename_nombre_vuelos_destino_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paquete',
        ),
        migrations.DeleteModel(
            name='vuelos',
        ),
    ]
