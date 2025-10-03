from django.db import models

class Task(models.Model):
    # Campos básicos
    title = models.CharField(max_length=255)  # Título de la tarea
    description = models.TextField()  # Descripción de la tarea
    completed = models.BooleanField(default=False)  # Estado de la tarea (completa o no)
    
    # Campos adicionales
    start_time = models.DateTimeField(null=True, blank=True)  # Fecha y hora en que la tarea debe comenzar (opcional)
    assigned_to = models.CharField(max_length=255, null=True, blank=True)  # Persona asignada (opcional)
    
    # Métodos adicionales
    def __str__(self):
        return self.title

    # Método para verificar si la tarea está completada
    def is_completed(self):
        return self.completed
