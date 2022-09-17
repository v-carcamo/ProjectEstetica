from django.db import models


class Servicios(models.Model):
    id_Servicio=models.BigAutoField(primary_key=True)
    nombre_Ser=models.CharField('Nombre', max_length=100)
    precio_Ser=models.CharField('Precio', max_length=100)
    descripcion_Ser=models.CharField('Descripción', max_length=15)
    