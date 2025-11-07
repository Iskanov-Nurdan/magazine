from rest_framework import viewsets
from apps.breand.models import Brend
from apps.breand.serializers import BrendSerializer

class BrendViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
