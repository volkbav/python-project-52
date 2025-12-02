from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UserTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(
            username="john",
            first_name="John",
            email="john@example.com",
        )
    
    # проверяем ответ от приложения users
    def test_user_list(self):
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")