from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('new/', views.hotel_new, name='hotel_new'),
    path('<int:pk>/edit/', views.hotel_edit, name='hotel_edit'),
    path('<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),
]
