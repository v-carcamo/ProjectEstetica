from django.contrib import admin
from .models.cliente import Clientes
from .models.productos import Productos


# Register your models here.

admin.site.register(Clientes)
admin.site.register(Productos)