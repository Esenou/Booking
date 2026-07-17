from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import BookingForm, HotelForm
from .models import Booking, Hotel


def hotel_list(request):
    hotels = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'hotel/hotel_list.html', {'hotels': hotels})


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotel/hotel_detail.html', {'hotel': hotel})


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
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = hotel
            if request.user.is_authenticated:
                booking.user = request.user
            if hotel.is_available(booking.check_in, booking.check_out):
                booking.save()
                messages.success(request, "Your booking request has been received.")
                return redirect('booking_detail', pk=booking.pk)
            else:
                form.add_error(None, "Sorry, this hotel is not available for the selected dates.")
    else:
        form = BookingForm()
    return render(request, 'hotel/booking_form.html', {'form': form, 'hotel': hotel})


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'hotel/booking_detail.html', {'booking': booking})


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
        messages.success(request, "Your booking has been cancelled.")
        return redirect('booking_list')
    return render(request, 'hotel/booking_cancel.html', {'booking': booking})
