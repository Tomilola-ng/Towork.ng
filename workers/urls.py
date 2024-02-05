from django.urls import path
from .views import createWorker, workerUpdate

urlpatterns = [
    path('', createWorker.as_view(), name='worker'),
    path('new/', createWorker.as_view(), name='worker-new'),
    path('<int:pk>/update/', workerUpdate.as_view(), name='worker-update'),
]
