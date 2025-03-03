from django.core.cache import cache

from config.settings import CACHE_ENABLED
from med_center.models import Product


class GetListProduct:
    """Класс обработки получения списка продуктов"""
    @staticmethod
    def get_list_product_from_cache():
        """Метод получает данные от БД, если списка продуктов нет в кэше, то добавляет его и возвращает список"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'product_list'
        products = cache.get(key)

        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products
