from rest_framework.generics import CreateAPIView
from .models import Task
from .serializers import TaskCreateSerializer

class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save(is_done=False)
