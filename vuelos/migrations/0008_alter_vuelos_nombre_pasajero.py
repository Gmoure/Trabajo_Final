# Generated by Django 4.1.2 on 2022-11-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0007_alter_vuelos_fecha_vuelo_ida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelos',
            name='nombre_pasajero',
            field=models.CharField(max_length=200),
        ),
    ]
