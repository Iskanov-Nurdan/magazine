from django.contrib import admin
from apps.base.models import BaseModel, Product, About
# Register your models here.

admin.site.register(BaseModel)
admin.site.register(Product)
admin.site.register(About)
