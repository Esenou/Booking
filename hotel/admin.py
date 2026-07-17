from django.contrib import admin

from .models import Booking, Hotel, Review


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'amount', 'capacity', 'published_date', 'author')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'text')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'guest_name', 'email', 'check_in', 'check_out', 'status', 'created_at')
    list_filter = ('status', 'check_in', 'hotel')
    search_fields = ('guest_name', 'email', 'hotel__title')
    date_hierarchy = 'check_in'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('hotel__title', 'user__username', 'text')
