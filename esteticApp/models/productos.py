from django.db import models


class Productos(models.Model):
    Id_Producto=models.BigAutoField(primary_key=True)
    Nombre_prod=models.CharField('Nombre_Producto', max_length=100)
    precio_prod=models.CharField('Precio_Producto', max_length=100)
    Contenido_neto=models.CharField('Contenido_neto', max_length=15)
    Descripcion_prod=models.CharField('Descripción', max_length=40, null=True)