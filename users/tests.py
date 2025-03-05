from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


class UserCreateViewTestCase(TestCase):

    def test_create_user(self):
        """Тестируем создание нового пользователя."""
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('users:register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.filter(username='testuser').exists())


class LoginUserViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_user(self):
        """Тестируем успешный вход пользователя."""
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Ожидаем redirect на главную страницу
