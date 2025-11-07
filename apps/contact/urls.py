
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contact.views import ContactViewSet 

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact') 

urlpatterns = [
    path('', include(router.urls)),
]