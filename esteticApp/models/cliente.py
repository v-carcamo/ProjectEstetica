from django.db import models


class Clientes(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombreCli=models.CharField('Nombre', max_length=100)
    apellido=models.CharField('Apellido', max_length=100)
    telefono=models.CharField('Telefono', max_length=15)
    email=models.CharField('E-mail', max_length=100)
    direccion=models.CharField('Direccion', max_length=40, null=True)