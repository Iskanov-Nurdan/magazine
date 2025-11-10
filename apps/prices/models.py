from django.db import models

class Price(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название прайса")
    file = models.FileField(upload_to='prices/', verbose_name="Файл")
    size_mb = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Размер (МБ)", null=True, blank=True)
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления")

    def save(self, *args, **kwargs):
        if self.file:
            self.size_mb = round(self.file.size / (1024 * 1024), 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
