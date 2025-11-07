from rest_framework.routers import DefaultRouter
from apps.base.views import BaseModelListCreateView, ProductListCreateView, AboutListCreateView

router = DefaultRouter()
router.register(r'base-models', BaseModelListCreateView, basename='base-model')
router.register(r'products', ProductListCreateView, basename='product')
router.register(r'about', AboutListCreateView, basename='about')

urlpatterns = router.urls
