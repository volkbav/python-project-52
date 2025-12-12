from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Label


# Create your tests here.
class LabelTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(
            name="label for tests"            
        )
        self.user = User.objects.create_user(
            username="Jonny",
            password="password123"  # NOSONAR
        )
        # входим в приложение под пользователем.
        self.client.login(username="Jonny", password="password123")  # NOSONAR
    
    def test_labels_list(self):
        response = self.client.get(reverse("labels:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "label for tests")
    
    def test_label_create(self):
        create_url = reverse(
            "labels:create",
        )
        list_url = reverse("labels:index")

        self.client.post(
            create_url,
            data={
                "name": "cteate test label"
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "cteate test label")
        self.assertContains(response, "label for tests")

    def test_label_update(self):
        update_url = reverse(
            "labels:update",
            kwargs={"pk": self.user.pk}
        )
        list_url = reverse("labels:index")

        self.client.post(
            update_url,
            data={
                "name": "update test label"
            }
        )
        response = self.client.get(list_url)
        
        self.assertContains(response, "update test label")
        self.assertNotContains(response, "label for tests")
        
    def test_label_delete(self):
        delete_url = reverse(
            "labels:delete",
            kwargs={"pk": self.user.pk}
        )
        list_url = reverse("labels:index")

        self.client.post(
            delete_url,
        )
        response = self.client.get(list_url)
        
        self.assertNotContains(response, "label for tests")
    

        
