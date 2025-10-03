from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),  # Listar tareas
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),  # Crear tarea
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # Obtener, actualizar o eliminar tarea por ID
]
