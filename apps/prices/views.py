from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import FileResponse, Http404
import os

from apps.prices.models import Price
from apps.prices.serializers import PriceSerializer


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Price.objects.all().order_by('-updated_at')
    serializer_class = PriceSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        """Скачивание файла"""
        obj = self.get_object()
        file_path = obj.file.path

        if not os.path.exists(file_path):
            raise Http404("Файл не найден")

        response = FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename=os.path.basename(file_path)
        )
        return response
