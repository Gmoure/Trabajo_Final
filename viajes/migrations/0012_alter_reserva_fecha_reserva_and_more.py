# Generated by Django 4.1.2 on 2022-11-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0011_alter_reserva_destino_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(max_length=100),
        ),
    ]