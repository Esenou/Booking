"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('hotel/', include('hotel.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Links from the original smartHotel theme redirect to the real pages.
    path('ru/rooms/', RedirectView.as_view(url='/hotel/', permanent=False)),
    path('ru/rooms', RedirectView.as_view(url='/hotel/', permanent=False)),
    path('ru/restaurant/', RedirectView.as_view(url='/', permanent=False)),
    path('ru/restaurant', RedirectView.as_view(url='/', permanent=False)),
    path('ru/', RedirectView.as_view(url='/', permanent=False)),
    path('ru', RedirectView.as_view(url='/', permanent=False)),
    path('en/', RedirectView.as_view(url='/', permanent=False)),
    path('en', RedirectView.as_view(url='/', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve the original smartHotel static HTML pages and assets from the project root.
urlpatterns += [
    path('<path:path>', serve, {'document_root': os.path.join(settings.BASE_DIR, 'smartHotel')}),
]
