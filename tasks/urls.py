from django.urls import path
from .views import TaskCreateAPIView

urlpatterns = [
    path("tasks/create/", TaskCreateAPIView.as_view(), name="task-create"),
]
