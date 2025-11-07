from rest_framework import serializers
from apps.about.models import About, AboutImage

# Сериализатор для изображений
class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ['id', 'image', 'description']

# Сериализатор для About с вложенными изображениями
class AboutSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['id', 'name', 'description', 'year', 'retail_outlets', 'trading_positions', 'images']
