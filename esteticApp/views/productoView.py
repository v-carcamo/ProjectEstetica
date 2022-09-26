from rest_framework import viewsets
from esteticApp.models.productos import Productos
from esteticApp.serializers import ProductoSerializer



class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Productos.objects.all()