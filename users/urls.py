from django.urls import path
from .views import dashboard, profileCreate, profileUpdate

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/create/', profileCreate.as_view(), name='profile-create'),
    path('profile/<int:pk>/update', profileUpdate.as_view(), name='profile-update'),
]
