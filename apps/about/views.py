from rest_framework import viewsets
from apps.about.models import About, AboutImage
from apps.about.serializers import AboutSerializer, AboutImageSerializer


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutImage.objects.all()
    serializer_class = AboutImageSerializer
