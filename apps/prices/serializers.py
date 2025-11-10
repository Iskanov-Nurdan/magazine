from rest_framework import serializers
from apps.prices.models import Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'title', 'file', 'size_mb', 'updated_at']
