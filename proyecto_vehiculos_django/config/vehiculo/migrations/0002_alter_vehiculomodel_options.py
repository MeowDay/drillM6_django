# Generated by Django 4.0.5 on 2023-07-27 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar el catálogo'),)},
        ),
    ]
