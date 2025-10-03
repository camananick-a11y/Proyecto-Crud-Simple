from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Vista para listar tareas
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Vista para crear tarea
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Vista para obtener, actualizar o eliminar tarea por ID
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
