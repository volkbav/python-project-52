from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UserTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="John",
            username="Jonny",
            password="password123"  # NOSONAR
        )
    
    # проверяем ответ от приложения users
    def test_user_list(self):
        response = self.client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")

    def test_user_update_flow(self):
        update_url = reverse(
            "users:update",
            kwargs={"pk": self.user.pk} 
        )
        list_url = reverse("users:index")

        # Отправка POST-запроса на изменение
        self.client.login(username="Jonny", password="password123")  # NOSONAR
        self.client.post(
            update_url,
            data={
                "username": "Bob",
                "password1": "password123",  # NOSONAR
                "password2": "password123",  # NOSONAR
            }
        )

        # Переход на страницу списка пользователей
        response = self.client.get(list_url)

        # Проверяем, что новое имя отрисовано в HTML
        self.assertContains(response, "Bob")
        self.assertNotContains(response, "John")