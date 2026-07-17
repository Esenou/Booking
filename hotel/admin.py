from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'amount', 'published_date', 'author')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'text')
