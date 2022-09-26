from django.contrib import admin
from esteticApp.models.cliente import Clientes
from esteticApp.models.productos import Productos
from esteticApp.models.servicios import Servicios
from esteticApp.models.ventas import Ventas


# Register your models here.

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Servicios)
admin.site.register(Ventas)