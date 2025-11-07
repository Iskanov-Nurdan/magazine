import django_filters
from apps.catalog.models import Product

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    sizes = django_filters.CharFilter(field_name="sizes", lookup_expr='iexact')


    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'sizes']
