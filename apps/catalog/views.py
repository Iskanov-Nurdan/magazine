from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.catalog.models import Product
from apps.catalog.serializers import ProductSerializer
from apps.catalog.pagination import CatalogPagination
from apps.catalog.filters import ProductFilter


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Список и создание товаров"""
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CatalogPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description', 'sizes']
    ordering_fields = ['price', 'title']
    ordering = ['id']


class ProductDetailView(viewsets.ReadOnlyModelViewSet):
    """Просмотр, редактирование и удаление конкретного товара"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
