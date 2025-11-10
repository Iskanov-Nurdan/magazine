from rest_framework.routers import DefaultRouter
from apps.base.views import BaseModelListCreateView, ProducttListCreateView, AbouttListCreateView

router = DefaultRouter()
router.register(r'base-models', BaseModelListCreateView, basename='base-model')
router.register(r'products', ProducttListCreateView, basename='product')
router.register(r'about',AbouttListCreateView , basename='about')

urlpatterns = router.urls
