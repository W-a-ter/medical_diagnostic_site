from django.db import models

from users.models import User


class Category(models.Model):
    """Модель создания таблицы в БД Категория"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    """Модель создания таблицы в БД Продукты"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')  # столбцы таблицы
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    picture = models.ImageField(upload_to='catalog/photo/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    is_publication = models.BooleanField(default=False, verbose_name='Статус публикации')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.price}$"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at']
        permissions = [
            ('can_unpublish_product', 'can unpublish product')
        ]
