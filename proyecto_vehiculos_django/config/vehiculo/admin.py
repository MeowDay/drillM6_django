from django.contrib import admin
from .models import VehiculoModel
from django.contrib.auth.models import Group, Permission

# Register your models here.

admin.site.register(VehiculoModel)
admin.site.unregister(Group)
admin.site.register(Group)