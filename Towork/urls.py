"""Towork URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django .conf.urls.static import static

from users.views import home as homeView
from users.views import register as registerView

urlpatterns = [
    path('auth/', admin.site.urls),

    # Authentication Views
    path('register/', registerView, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/social/", include("allauth.urls")),

    # User Views
    path('dashboard/', include('users.urls')),

    # Worker Views
    path('worker/', include('workers.urls')),

    # Seek Views
    path('seek/', include('seek.urls')),

    # Redirect View
    path('', homeView, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
