from django.urls import path
from django.views.decorators.cache import cache_page

from med_center.apps import MedCenterConfig

app_name = MedCenterConfig.name

from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CatalogListView, CatalogDetailView, CatalogTemplateView, CatalogCreateView, ProductUpdateView, \
    ProductDeleteView, ProductCategoryView

app_name = 'catalog'


urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', CatalogDetailView.as_view(), name='product'),
    path('add_product/', CatalogCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('category/<int:pk>/', cache_page(60)(ProductCategoryView.as_view()), name='product_category'),
]