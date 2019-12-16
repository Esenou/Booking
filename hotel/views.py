from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect

from hotel.models import Hotel


def hotel_list(request):
    hotels = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/hotel_list.html',{'hotels':hotels })