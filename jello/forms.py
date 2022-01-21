from .models import Customer, Product
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # exclude = ('products',)
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }
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
