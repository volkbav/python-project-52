from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Status


# Create your tests here.
class StatusTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(
            name="status for tests"            
        )
        self.user = User.objects.create_user(
            username="Jonny",
            password="password123"  # NOSONAR
        )
        # входим в приложение под пользователем.
        self.client.login(username="Jonny", password="password123")  # NOSONAR
    
    def test_statuses_list(self):
        response = self.client.get(reverse("statuses:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "status for tests")
    
    def test_status_create(self):
        create_url = reverse(
            "statuses:create",
        )
        list_url = reverse("statuses:index")

        self.client.post(
            create_url,
            data={
                "name": "create test status"
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "create test status")
        self.assertContains(response, "status for tests")

    def test_status_update(self):
        update_url = reverse(
            "statuses:update",
            kwargs={"pk": self.user.pk}
        )
        list_url = reverse("statuses:index")

        self.client.post(
            update_url,
            data={
                "name": "update test status"
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "update test status")
        self.assertNotContains(response, "status for tests")
        
    def test_status_delete(self):
        delete_url = reverse(
            "statuses:delete",
            kwargs={"pk": self.user.pk}
        )
        list_url = reverse("statuses:index")

        self.client.post(
            delete_url,
        )
        response = self.client.get(list_url)
        
        self.assertNotContains(response, "status for tests")
    

        
