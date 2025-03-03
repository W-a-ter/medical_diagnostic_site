from django.forms import ModelForm
from django.core.exceptions import ValidationError

from med_center.models import Schedule


class ProductForm(ModelForm):
    """Класс создания формы добавления продуктов"""
    class Meta:
        model = Schedule
        exclude = ('is_publication', 'owner')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['doctor'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        # self.fields['speciality'].widget.attrs.update({
        #     'class': 'form-select'
        # })
        # self.fields['data'].widget.attrs.update({
        #     'class': 'form-select'
        # })

#     def clean(self):
#         """Валидация данных названия и описания (не должны иметь запрещенные слова)"""
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         description = cleaned_data.get('description')
#         banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
#
#         for word in banned_words:
#             if word in name.lower():
#                 self.add_error('name', f'Нельзя использовать слово "{word.title()}" в названии.')
#             if word in description.lower():
#                 self.add_error('description', f'Нельзя использовать слово "{word.title()}" в описании.')
#
#     def clean_price(self):
#         """Валидация стоимости продукта"""
#         price = self.cleaned_data.get('price')
#
#         if int(price) <= 0:
#             raise ValidationError("Цена должна быть положительная")
#         return price
#
#
class ProductModerForm(ProductForm, ModelForm):
    class Meta:
        model = Schedule
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super(ProductModerForm, self).__init__(*args, **kwargs)

        self.fields['is_publication'].widget.attrs.update({
            'class': 'form-check-input'
        })
