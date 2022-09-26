from rest_framework import viewsets
from esteticApp.models.servicios import Servicios
from esteticApp.serializers import ServicioSerializer



class ServicioView(viewsets.ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicios.objects.all()