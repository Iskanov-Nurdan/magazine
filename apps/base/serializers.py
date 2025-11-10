from rest_framework import serializers
from apps.base.models import BaseModel, Product, About

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'

class ProducttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AbouttSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
