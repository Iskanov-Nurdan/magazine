from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name="название")
    image = models.ImageField(upload_to="products", verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (сом)")
    sizes = models.CharField(max_length=10, verbose_name="Размер")
    quantities = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"