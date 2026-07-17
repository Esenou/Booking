from django.conf import settings
from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hotel_images/%Y/%m/%d', blank=True, null=True)
    text = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
