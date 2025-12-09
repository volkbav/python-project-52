# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status

from .models import Task


class TaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Jonny",
            password="password123"  # NOSONAR
        )
        self.task = Task.objects.create(
            name="task for tests",
            status=Status.objects.create(
                name="status for tests"
            ),
            author=User.objects.get(username='Jonny'),
            description="test description",
            executor=None,
        )
        
        # входим в приложение под пользователем.
        self.client.login(username="Jonny", password="password123")  # NOSONAR
    
    def test_task_list(self):
        response = self.client.get(reverse("tasks:tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "task for tests")
    
    def test_status_create(self):
        create_url = reverse("tasks:create")
        list_url = reverse("tasks:tasks")
        status = Status.objects.get(name="status for tests")

        self.client.post(
            create_url,
            data={
                "name": "my task for tests",
                "status": status.id,
                "author": self.user.pk,
                "description": "test description",
                "executor": "",
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "my task for tests")
        self.assertContains(response, "task for tests")

    def test_task_update(self):
        update_url = reverse(
            "tasks:update",
            kwargs={"pk": self.task.pk}
        )

        list_url = reverse("tasks:tasks")

        self.client.post(
            update_url,
            data={
                "name": "update tasks test",
                "status": self.task.status.pk,
                "author": self.user.pk,
                "description": "test description",
                "executor": "",
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "update tasks test")
        self.assertNotContains(response, "task for tests")
        
    def test_status_delete(self):
        delete_url = reverse(
            "tasks:delete",
            kwargs={"pk": self.user.pk}
        )
        list_url = reverse("tasks:tasks")

        self.client.post(
            delete_url,
        )
        response = self.client.get(list_url)
        
        self.assertNotContains(response, "task for tests")
    

        
