from django.db import models

class About(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year = models.IntegerField(verbose_name="Год")
    retail_outlets = models.CharField(max_length=255, verbose_name="Товарных точек")
    trading_positions = models.CharField(max_length=255, verbose_name="Торговых позиций")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.about.name}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"