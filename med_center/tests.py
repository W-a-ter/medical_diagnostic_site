from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Product


class MedCenterTestCase(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.product = Product.objects.create(name='product')

    def test_home_page_get(self):
        """Тестируем GET запрос на главную страницу."""
        response = self.client.get(reverse('med_center:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'med_center/home.html')

    def test_product_detail_view(self):
        """Тестируем доступ к детали продукта."""
        response = self.client.get(reverse('med_center:product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'med_center/product_detail.html')

    def test_visit_result_view(self):
        """Тестируем представление статистики посещений."""
        response = self.client.get(reverse('med_center:visit_result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'med_center/visit_result.html')
