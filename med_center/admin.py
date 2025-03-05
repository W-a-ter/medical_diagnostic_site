from django.contrib import admin
from .models import Product, Doctor


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Продуктов в админке"""

    list_display = (
        "id",
        "name",
        "price",
    )
    list_filter = ("id", "name", "price")
    search_fields = ("id", "name", "price")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) врачей в админке"""

    list_display = ("id", "speciality")
    list_filter = ("id", "speciality")
    search_fields = ("id", "speciality")
