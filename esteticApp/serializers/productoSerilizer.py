from rest_framework import serializers
from esteticApp.models import Productos


class ProductoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Productos
            fields = ['Id_Producto','Nombre_prod', 'precio_prod', 'Contenido_neto', 'Descripcion_prod']