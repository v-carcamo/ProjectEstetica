from rest_framework import serializers
from esteticApp.models import Clientes
from esteticApp.serializers.ventaSerializer import VentaSerializer

class ClienteSerializer(serializers.ModelSerializer):
        ventas = VentaSerializer(many=True, read_only=True)
        class Meta:
            model = Clientes
            fields = ['id', 'username', 'password', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'ventas']