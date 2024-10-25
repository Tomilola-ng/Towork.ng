""" Workers URLs """
from django.urls import path
from .views import CreateWorker, WorkerUpdate

urlpatterns = [
    path('', CreateWorker.as_view(), name='worker'),
    path('new/', CreateWorker.as_view(), name='worker-new'),
    path('<int:pk>/update/', WorkerUpdate.as_view(), name='worker-update'),
]
