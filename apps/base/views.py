from rest_framework import viewsets
from apps.base.serializers import BaseModelSerializer, ProducttSerializer, AbouttSerializer
from apps.base.models import BaseModel, Product, About

class BaseModelListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = BaseModel.objects.all()
    serializer_class = BaseModelSerializer

class ProducttListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProducttSerializer


class AbouttListCreateView(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AbouttSerializer
