from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import HotelForm
from .models import Hotel


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
