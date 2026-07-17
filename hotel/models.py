from django.conf import settings
from django.core.exceptions import ValidationError
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

    def occupied_rooms(self, check_in, check_out, exclude_booking=None):
        """Return the maximum number of overlapping confirmed/pending bookings
        for any night in the requested range.
        """
        bookings = self.bookings.filter(
            status__in=(Booking.Status.PENDING, Booking.Status.CONFIRMED),
            check_in__lt=check_out,
            check_out__gt=check_in,
        )
        if exclude_booking:
            bookings = bookings.exclude(pk=exclude_booking.pk)

        if not bookings.exists():
            return 0

        events = []
        for booking in bookings:
            events.append((booking.check_in, 1))
            events.append((booking.check_out, -1))
        events.sort()

        current = 0
        max_occupied = 0
        for _date, delta in events:
            current += delta
            max_occupied = max(max_occupied, current)
        return max_occupied

    def is_available(self, check_in, check_out, exclude_booking=None):
        return self.occupied_rooms(check_in, check_out, exclude_booking) < self.amount


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    guest_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.guest_name} — {self.hotel.title} ({self.check_in} - {self.check_out})"

    def clean(self):
        if self.check_in and self.check_out:
            if self.check_in >= self.check_out:
                raise ValidationError("Check-out date must be after check-in date.")
            if self.check_in < timezone.now().date():
                raise ValidationError("Check-in date cannot be in the past.")
        if self.hotel and self.pk is None:
            if not self.hotel.is_available(self.check_in, self.check_out):
                raise ValidationError("This hotel is not available for the selected dates.")
        elif self.hotel and self.pk:
            if not self.hotel.is_available(self.check_in, self.check_out, exclude_booking=self):
                raise ValidationError("This hotel is not available for the selected dates.")
