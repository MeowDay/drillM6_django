# Generated by Django 4.2.2 on 2023-07-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('fiat', 'Fiat'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('toyota', 'Toyota')], default='ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serialCarroceria', models.CharField(max_length=50)),
                ('serialMotor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='particular', max_length=20)),
                ('precio', models.FloatField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('visualizar_catalogo', 'puede visualizar_catalogo'),),
            },
        ),
    ]