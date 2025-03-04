from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (CatalogListView, CatalogDetailView, CatalogTemplateView, CatalogCreateView, ProductUpdateView, \
                    ProductDeleteView, ScheduleDeleteView, ScheduleCreateView, ScheduleListView, AboutPageView,
                    ProductListView,
                    VisitResultListView, ScheduleConfirmedView)

app_name = 'med_center'


urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),

    path('product/<int:pk>', CatalogDetailView.as_view(), name='product_detail'),
    path('add_product/', CatalogCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_list/', ProductListView.as_view(), name='product_list'),

    path('schedule/<int:pk>', ScheduleListView.as_view(), name='schedule'),
    path('schedule_create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),

    path('about/', AboutPageView.as_view(), name='about'),
    path('visit_result/', VisitResultListView.as_view(), name='visit_result'),
    path('schedule-confirmed/', ScheduleConfirmedView.as_view(), name='schedule_confirmed'),
]
