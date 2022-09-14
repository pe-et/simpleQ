from django.conf import settings
from django.db import models
from django.urls import reverse
from django_cryptography.fields import encrypt


class Queue(models.Model):
    first_name = encrypt(models.CharField(max_length=255))
    last_name = encrypt(models.CharField(max_length=255))
    email = encrypt(models.EmailField(max_length=254))
    phone_number = encrypt(models.CharField(max_length=255))
    date = models.DateTimeField(auto_now_add=True)
    notes = encrypt(models.TextField(blank=True))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.pk}"

    def get_absolute_url(self):
        return reverse("queue_detail", kwargs={"pk": self.pk})
