from django.db import models

from users.models import User


class Doctor(models.Model):
    username = models.CharField(blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    speciality = models.CharField(
        max_length=30,
        verbose_name="Специальность",
        default="Терапевт",
        choices=[
            ("Терапевт", "Терапевт"),
            ("Невролог", "Невролог"),
            ("Эндокринолог", "Эндокринолог"),
            ("Косметолог", "Косметолог"),
        ]
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Product(models.Model):
    """Модель создания таблицы в БД Услуги"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')  # столбцы таблицы
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    picture = models.ImageField(upload_to='media/catalog/photo/', verbose_name='Изображение', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return f"{self.name} - {self.price}$"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price',]
        permissions = [
            ('can_unpublish_product', 'can unpublish product')
        ]


class Schedule(models.Model):
    """Модель записи на прием"""
    date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата записи"
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="doctor",
        verbose_name="ФИО врача",
        null=True, blank=True
    )
    speciality = models.CharField(
        max_length=9,
        verbose_name="направление",
        default="Терапевт",
        choices=[
            ("Терапевт", "Терапевт"),
            ("Невролог", "Невролог"),
            ("Эндокринолог", "Эндокринолог"),
            ("Косметолог", "Косметолог"),
        ]
    ),
    owner = models.ForeignKey(User,
        on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Владелец')

    def __str__(self):
        return f"№ {self.id}"

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"
        ordering = [
            "date",
            "doctor",
        ]
        permissions = [
            ('can_view_mailing', 'can view mailing')
        ]


class VisitResult(models.Model):
    """Модель результата приема"""

    objects = None

    date = models.DateTimeField(
        blank=True, null=True, verbose_name="Время приема"
    )
    description = models.CharField(
        max_length=500, verbose_name='Описание',
        null=True, blank=True,
    )

    owner = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='владелец', blank=True,
        null=True, verbose_name='Владелец'
    )

    def __str__(self):
        return f"№ {self.id}"

    class Meta:
        verbose_name = "результат посещения"
        verbose_name_plural = "результаты посещения"
