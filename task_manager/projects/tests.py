
# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Project


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Jonny",
            password="password123",  # NOSONAR
        )
        status=Status.objects.create(name="status for tests")
        label=Label.objects.create(name="label for tests")

        self.project = Project.objects.create(
            name="project for tests",
            description="test description",
            author=User.objects.get(username='Jonny'),
            executor=None,
            status=status,
            start_date=None,
            deadline=None,
            is_active=True
        )

        self.project.labels.set([label])
        
        # входим в приложение под пользователем.
        self.client.login(username="Jonny", password="password123")  # NOSONAR
    
    def test_project_list(self):
        response = self.client.get(reverse("projects:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "project for tests")
        self.assertContains(response, "status for tests")

    
    def test_project_create(self):
        create_url = reverse("projects:create")
        list_url = reverse("projects:index")
        status = Status.objects.get(name="status for tests")
        label = Label.objects.get(name="label for tests")

        response = self.client.post(
            create_url,
            data={
                "name": "my project for tests",
                "description": "test description",
                "author": self.user.pk,
                "executor": "",
                "status": status.id,
                "labels": label.id,
                "is_active": True,
            }
        )

        self.assertEqual(response.status_code, 302)

        first_response = self.client.get(list_url)
        self.assertContains(first_response, "my project for tests")
        self.assertContains(first_response, "status for tests")
        self.assertContains(first_response, "label for tests")

        new_project = Project.objects.get(name="my project for tests")
        project_url = reverse(
            "projects:project",
            kwargs={"pk": new_project.pk}
        )
        second_response = self.client.get(project_url)
        self.assertContains(second_response, "my project for tests")
        self.assertContains(second_response, "status for tests")
        self.assertContains(second_response, "label for tests")
        self.assertContains(second_response, "label for tests")





    def test_project_update(self):
        update_url = reverse(
            "projects:update",
            kwargs={"pk": self.project.pk}
        )

        # list_url = reverse("projects:index")
        
        status = Status.objects.get(name="status for tests")
        label = Label.objects.get(name="label for tests")

        self.client.post(
            update_url,
            data={
                "name": "project for tests",
                "description": "update projects test",
                "author": self.user.pk,
                "executor": "",
                "status": status.id,
                "labels": label.id,
                "is_active": True,
            }
        )
        response = self.client.get(update_url)
        
        self.assertContains(response, "project for tests")
        self.assertContains(response, "update projects test")
        self.assertNotContains(response, "my project for tests")
        self.assertNotContains(response, "test description")

        
    def test_project_delete(self):
        delete_url = reverse(
            "projects:delete",
            kwargs={"pk": self.project.pk}
        )
        list_url = reverse("projects:index")

        self.client.post(
            delete_url,
        )
        response = self.client.get(list_url)
        
        self.assertNotContains(response, "project for tests")
    

        
