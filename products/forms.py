from django import forms
from django.core.files import File
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(required=True)
    photo = forms.FileField()
    price = forms.DecimalField(required=True, initial=199)
    # photo = forms.FloatField()

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'stock',
            'photo',
        ]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if "CFE" in name:
            return name
        else:
            raise forms.ValidationError("This is not a valid Name.")

    # def clean_email(self, *args,**kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not valid email.")
    #     return email


class RawProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.DecimalField(required=True, initial=199)
    stock = forms.FloatField(initial=200)
    photo = forms.ImageField()

