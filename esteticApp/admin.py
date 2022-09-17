from django.contrib import admin
from .models.cliente import Clientes
from .models.servicios import Servicios


# Register your models here.

admin.site.register(Clientes)
admin.site.register(Servicios)