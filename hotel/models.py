from django.conf import settings
from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=True)
    text = models.TextField()
    price=models.TextField()
    amount=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


