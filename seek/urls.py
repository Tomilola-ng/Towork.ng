from django.urls import path
from .views import seekCreate, seekList, seekDetail

urlpatterns = [
    path('', seekList.as_view(), name='seek'),
    path('new/', seekCreate.as_view(), name='seek-new'),
    path('<int:pk>/detail/', seekDetail.as_view(), name='seek-detail'),
]
