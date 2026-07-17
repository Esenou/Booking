from django.conf import settings
from django.core.mail import send_mail


def send_booking_notification(booking, subject, body):
    recipient = booking.email
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        fail_silently=True,
    )
