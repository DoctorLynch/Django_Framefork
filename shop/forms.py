from django import forms

from shop.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image_preview', 'category', 'purchase_price',
                  'date_creation', 'date_last_mod')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' \
                or 'обман' or 'полиция' or 'радар' in cleaned_data:
            raise forms.ValidationError('Содержится запрещенный продукт')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' \
                or 'обман' or 'полиция' or 'радар' in cleaned_data:
            raise forms.ValidationError('Содержится запрещенный продукт')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'num_of_version', 'name_version', 'flag_of_version')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

        def clean_product(self):
            cleaned_data = self.cleaned_data['product']

            if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' \
                    or 'обман' or 'полиция' or 'радар' in cleaned_data:
                raise forms.ValidationError('Содержится запрещенный продукт')

            return cleaned_data
