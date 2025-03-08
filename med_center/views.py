from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from med_center.services import GetListProduct
from .forms import ProductForm, ProductModerForm, ScheduleForm
from .models import Product, Schedule, Doctor, VisitResult


class CatalogListView(ListView):
    """Класс представления каталога товаров на главной странице"""

    model = Product
    template_name = "med_center/home.html"
    context_object_name = "product"

    def get_queryset(self):
        return GetListProduct.get_list_product_from_cache()


class ProductListView(ListView):
    """Класс представления каталога товаров на отдельной странице"""

    model = Product
    template_name = "med_center/product_list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return GetListProduct.get_list_product_from_cache()


@method_decorator(cache_page(60), name="dispatch")
class CatalogDetailView(DetailView):
    """Класс представления полной информации о товаре, на отдельной странице"""

    model = Product
    template_name = "med_center/product_detail.html"
    context_object_name = "product"


class CatalogCreateView(LoginRequiredMixin, CreateView):
    """контроллер Создание продукта"""

    model = Product
    template_name = "med_center/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm
    success_url = reverse_lazy("med_center:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения продукта"""

    model = Product
    template_name = "med_center/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm

    def get_success_url(self):
        return reverse("med_center:product", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        """
        Проверка чтобы пользователь был владельцем продукта и тогда может его изменять
        и если у пользовтаеля есть право can_unpublish_product
        """
        user = self.request.user
        if user.has_perm("med_center.can_unpublish_product"):
            return ProductModerForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления продукта"""

    model = Schedule
    context_object_name = "product_delete"

    success_url = reverse_lazy("med_center:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("med_center.delete_product"):
            return super().get_form_class()
        raise PermissionDenied


class CatalogTemplateView(TemplateView):
    """Класс представления обратной связи с заполнением формы"""

    template_name = "med_center/contacts.html"

    def post(self, request, *args, **kwargs):
        """Обрабатываем форму и возвращаем ответ"""
        if self.request.method == "POST":
            # Получение данных из формы
            name = request.POST.get("name")
            # Обработка данных (например, сохранение в БД, отправка email и т. д.)
            # Здесь мы просто возвращаем простой ответ
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return render(request, "med_center/contacts.html")


class ScheduleListView(ListView):
    """Класс представления записи на прием в ЛК пользователя"""

    model = Schedule
    template_name = "med_center/schedule.html"
    context_object_name = "schedule"


class ScheduleCreateView(LoginRequiredMixin, CreateView):
    """контроллер Создание продукта"""

    model = Schedule
    template_name = "med_center/schedule_create.html"
    context_object_name = "schedule_create"

    form_class = ScheduleForm
    success_url = reverse_lazy("med_center:schedule_confirmed")


class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления записи на прием"""

    model = Schedule
    context_object_name = "schedule_delete"

    success_url = reverse_lazy("med_center:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("med_center.delete_product"):
            return super().get_form_class()
        raise PermissionDenied


class DoctorListView(ListView):
    model = Doctor
    template_name = "med_center/about.html"
    context_object_name = "doctors"

    def get_queryset(self):
        return Doctor.objects.filter()


class VisitResultListView(ListView):
    """Класс представления результатов приема на странице"""

    model = VisitResult
    template_name = "med_center/visit_result.html"
    context_object_name = "visit"

    def get_queryset(self):
        return Schedule.objects.filter()


class ScheduleConfirmedView(TemplateView):
    """Подтверждение записи"""

    template_name = "med_center/schedule_confirmed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ваш электронный адрес активирован"
        return context
