# Generated by Django 4.1.2 on 2022-11-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0004_alter_vuelos_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='vuelos',
            name='nombre_vuelo',
            field=models.CharField(default='', max_length=200),
        ),
    ]