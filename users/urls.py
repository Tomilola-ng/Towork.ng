""" User URLs """
from django.urls import path
from .views import dashboard, ProfileCreate, ProfileUpdate

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/create/', ProfileCreate.as_view(), name='profile-create'),
    path('profile/<int:pk>/update', ProfileUpdate.as_view(), name='profile-update'),
]
