from django.db import models
from esteticApp.models.cliente import Clientes
from esteticApp.models.productos import Productos
from esteticApp.models.servicios import Servicios

class Ventas(models.Model):
    Id_venta = models.BigIntegerField(primary_key=True, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, related_name='ventas', on_delete = models.CASCADE)
    producto = models.ForeignKey(Productos, blank=True, null=True, related_name='ventas', on_delete = models.CASCADE)
    servicio = models.ForeignKey(Servicios, blank=True, null=True, related_name='ventas', on_delete = models.CASCADE)