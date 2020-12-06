from django.db import models
from django.contrib.auth.models import User


class Ksiazka(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Moje-ksiazki"

    def __str__(self):
        return self.title


