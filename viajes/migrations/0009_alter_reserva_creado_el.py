# Generated by Django 4.1.2 on 2022-11-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0008_alter_reserva_creado_el'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='creado_el',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]