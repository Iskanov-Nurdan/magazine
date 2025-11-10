# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import FileResponse, HttpResponse
import io, csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        """Скачать заказ в PDF"""
        order = self.get_object()

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        p.drawString(100, 800, f"Заказ №{order.id}")
        p.drawString(100, 780, f"Дата: {order.created_at.strftime('%d.%m.%Y %H:%M')}")
        p.drawString(100, 760, f"Сумма: {order.total_amount} сом")
        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=f"order_{order.id}.pdf")

    @action(detail=True, methods=['get'])
    def excel(self, request, pk=None):
        """Скачать заказ в Excel (CSV-формат)"""
        order = self.get_object()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="order_{order.id}.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Дата', 'Сумма'])
        writer.writerow([order.id, order.created_at.strftime('%d.%m.%Y %H:%M'), order.total_amount])

        return response
