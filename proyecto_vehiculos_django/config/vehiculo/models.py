from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.
MARCA_OPCIONES = [
    ('fiat', 'Fiat'),
    ('chevrolet', 'Chevrolet'),
    ('ford', 'Ford'),
    ('toyota', 'Toyota'),
]
CATEGORIA_OPCIONES = [
    ('Particular', 'Particular'),
    ('Transporte', 'Transporte'),
    ('Carga', 'Carga'),
]
class VehiculoModel(models.Model):
    marca = models.CharField(max_length=20, choices=MARCA_OPCIONES, default='ford')
    modelo = models.CharField(max_length=100)   
    serialCarroceria = models.CharField(max_length=50)
    serialMotor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_OPCIONES, default='particular')
    precio = models.FloatField() 
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("visualizar_catalogo", "Puede visualizar el catálogo"),("can_add_vehiculo_model", "Puede agregar vehiculos al catálogo"),
  
        )
    
    def __str__(self):
        return self.marca