""" Seek Artisans URLs """
from django.urls import path
from .views import SeekCreate, SeekList, SeekDetail

urlpatterns = [
    path('', SeekList.as_view(), name='seek'),
    path('new/', SeekCreate.as_view(), name='seek-new'),
    path('<int:pk>/detail/', SeekDetail.as_view(), name='seek-detail'),
]
