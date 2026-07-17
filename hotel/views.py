from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import BookingForm, HotelForm, HotelSearchForm, ReviewForm
from .models import Booking, Hotel, Review
from .utils import send_booking_notification


def hotel_list(request):
    hotels = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    form = HotelSearchForm(request.GET)

    if form.is_valid():
        data = form.cleaned_data
        if data.get('min_price') is not None:
            hotels = hotels.filter(price__gte=data['min_price'])
        if data.get('max_price') is not None:
            hotels = hotels.filter(price__lte=data['max_price'])
        if data.get('guests'):
            hotels = hotels.filter(capacity__gte=data['guests'])

        check_in = data.get('check_in')
        check_out = data.get('check_out')
        if check_in and check_out:
            hotels = [h for h in hotels if h.is_available(check_in, check_out)]

    return render(request, 'hotel/hotel_list.html', {'hotels': hotels, 'form': form})


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel.objects.prefetch_related('reviews__user'), pk=pk)
    reviews = hotel.reviews.all()
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    return render(request, 'hotel/hotel_detail.html', {
        'hotel': hotel,
        'reviews': reviews,
        'user_review': user_review,
    })


@login_required
def hotel_new(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.author = request.user
            hotel.published_date = timezone.now()
            hotel.save()
            return redirect('hotel_detail', pk=hotel.pk)
    else:
        form = HotelForm()
    return render(request, 'hotel/hotel_edit.html', {'form': form})


@login_required
def hotel_edit(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.user != hotel.author:
        return redirect('hotel_list')
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.published_date = timezone.now()
            hotel.save()
            return redirect('hotel_detail', pk=hotel.pk)
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel/hotel_edit.html', {'form': form})


@login_required
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.user != hotel.author:
        return redirect('hotel_list')
    if request.method == "POST":
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/hotel_confirm_delete.html', {'hotel': hotel})


def booking_create(request, hotel_pk):
    hotel = get_object_or_404(Hotel, pk=hotel_pk)
    if request.method == "POST":
        form = BookingForm(request.POST, hotel=hotel)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = hotel
            if request.user.is_authenticated:
                booking.user = request.user
            if hotel.is_available(booking.check_in, booking.check_out):
                booking.save()
                send_booking_notification(
                    booking,
                    subject=f"Booking request received — {hotel.title}",
                    body=(
                        f"Hi {booking.guest_name},\n\n"
                        f"Your booking request for {hotel.title} from {booking.check_in} "
                        f"to {booking.check_out} has been received.\n"
                        f"Status: {booking.get_status_display()}\n\n"
                        f"We will contact you shortly to confirm.\n"
                    ),
                )
                messages.success(request, "Your booking request has been received.")
                return redirect('booking_detail', pk=booking.pk)
            else:
                form.add_error(None, "Sorry, this hotel is not available for the selected dates.")
    else:
        form = BookingForm(hotel=hotel)
    return render(request, 'hotel/booking_form.html', {'form': form, 'hotel': hotel})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'hotel/booking_detail.html', {'booking': booking})


@login_required
def add_review(request, hotel_pk):
    hotel = get_object_or_404(Hotel, pk=hotel_pk)
    review, created = Review.objects.get_or_create(hotel=hotel, user=request.user, defaults={'rating': 5, 'text': ''})
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been saved.")
            return redirect('hotel_detail', pk=hotel.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'hotel/review_form.html', {'form': form, 'hotel': hotel})


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hotel/booking_list.html', {'bookings': bookings})


@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.status = Booking.Status.CANCELLED
        booking.save()
        send_booking_notification(
            booking,
            subject=f"Booking cancelled — {booking.hotel.title}",
            body=(
                f"Hi {booking.guest_name},\n\n"
                f"Your booking at {booking.hotel.title} from {booking.check_in} "
                f"to {booking.check_out} has been cancelled.\n\n"
                f"If you did not request this, please contact us.\n"
            ),
        )
        messages.success(request, "Your booking has been cancelled.")
        return redirect('booking_list')
    return render(request, 'hotel/booking_cancel.html', {'booking': booking})
