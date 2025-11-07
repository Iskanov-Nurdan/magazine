from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.about.views import AboutViewSet, AboutImageViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'about-images', AboutImageViewSet)

urlpatterns = router.urls