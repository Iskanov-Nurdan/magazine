
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.prices.views import PriceViewSet 

router = DefaultRouter()
router.register(r'price', PriceViewSet, basename='price') 

urlpatterns = [
    path('', include(router.urls)),
]