from rest_framework import serializers
from esteticApp.models import Ventas


class VentaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ventas
            fields = ['Id_venta','fecha', 'producto', 'servicio', 'cliente']