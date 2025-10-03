from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskModelTests(TestCase):

    def setUp(self):
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test task description',
            'completed': False,
            'start_time': '2025-01-01T10:00:00Z',
            'assigned_to': 'John Doe'
        }
        self.client = APIClient()

    def test_create_task(self):
        response = self.client.post('/api/tasks/create/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.task_data['title'])
        self.assertEqual(response.data['description'], self.task_data['description'])

    def test_read_task(self):
        task = Task.objects.create(**self.task_data)
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)

    def test_update_task(self):
        task = Task.objects.create(**self.task_data)
        updated_data = {'title': 'Updated Task Title'}
        response = self.client.patch(f'/api/tasks/{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task Title')

    def test_delete_task(self):
        task = Task.objects.create(**self.task_data)
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
