from django.db import models

class BaseModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Базовая модель"
        verbose_name_plural = "Базовые модели"

class Product(models.Model):
    image = models.ImageField(upload_to="products", verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    

class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="about", verbose_name="Изображение")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"