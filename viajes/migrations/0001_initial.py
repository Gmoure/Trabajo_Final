# Generated by Django 4.1.2 on 2022-10-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_reserva', models.IntegerField()),
                ('hora_reserva', models.IntegerField()),
            ],
        ),
    ]
