
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrendViewSet 

router = DefaultRouter()
router.register(r'brands', BrendViewSet, basename='brand') 

urlpatterns = [
    path('', include(router.urls)),
]