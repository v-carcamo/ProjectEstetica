from rest_framework import viewsets
from esteticApp.serializers import VentaSerializer
from esteticApp.models import Ventas


class VentasView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Ventas.objects.all()
    