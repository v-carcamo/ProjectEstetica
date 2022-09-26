from rest_framework import serializers
from esteticApp.models import Servicios


class ServicioSerializer(serializers.ModelSerializer):
        class Meta:
            model = Servicios
            fields = ['Id_Servicio','nombre_Ser', 'precio_Ser', 'descripcion_Ser']