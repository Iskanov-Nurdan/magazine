from rest_framework import serializers
from apps.breand.models import Brend

class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ['id', 'name', 'image']