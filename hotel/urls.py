from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('new/', views.hotel_new, name='hotel_new'),
    path('my-bookings/', views.booking_list, name='booking_list'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:pk>/cancel/', views.booking_cancel, name='booking_cancel'),
    path('<int:hotel_pk>/book/', views.booking_create, name='booking_create'),
    path('<int:pk>/edit/', views.hotel_edit, name='hotel_edit'),
    path('<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
]
