from django.db import models
#from django.contrib.auth.models import User
from django.urls import reverse


class Method(models.Model):
    title = models.TextField(
        verbose_name="Название", max_length=30
    )

    class Meta:
        verbose_name = "Метод"
        verbose_name_plural = "Методы"
        db_table = 'method'
    
    def __str__(self):
        return f"Метод {self.pk}"
'''
    def get_absolute_url(self):
        return reverse("add_categor")
'''