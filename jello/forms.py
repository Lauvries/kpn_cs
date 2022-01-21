from .models import Customer, Product
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            "date_of_birth": DateInput()
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "name": "Product Name"
        }
