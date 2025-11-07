from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    address_url = models.URLField(verbose_name="URL адрес")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    