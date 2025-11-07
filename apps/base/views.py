from rest_framework import viewsets
from apps.base.serializers import BaseModelSerializer, ProductSerializer, AboutSerializer
from apps.base.models import BaseModel, Product, About

class BaseModelListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = BaseModel.objects.all()
    serializer_class = BaseModelSerializer

class ProductListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class AboutListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
