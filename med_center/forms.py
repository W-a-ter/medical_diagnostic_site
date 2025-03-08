from django.forms import ModelForm

from med_center.models import Schedule, Product


class ProductForm(ModelForm):
    """Класс создания формы добавления продуктов"""

    class Meta:
        model = Product
        exclude = ("is_publication", "owner")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )
        self.fields["price"].widget.attrs.update({"class": "form-select"})
        self.fields["description"].widget.attrs.update({"class": "form-select"})


class ProductModerForm(ProductForm, ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        super(ProductModerForm, self).__init__(*args, **kwargs)

        self.fields["price"].widget.attrs.update({"class": "form-check-input"})


class ScheduleForm(ModelForm):
    """Класс создания формы записи на прием"""

    class Meta:
        model = Schedule
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

        self.fields["date"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите желаемую дату приема"}
        )
        self.fields["doctor"].widget.attrs.update({"class": "form-select"})


class ScheduleModerForm(ScheduleForm, ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        super(ScheduleModerForm, self).__init__(*args, **kwargs)

        self.fields["date"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите желаемую дату приема"}
        )
        self.fields["doctor"].widget.attrs.update({"class": "form-select"})
        self.fields["speciality"].widget.attrs.update({"class": "form-select"})
