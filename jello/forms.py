from .models import Customer
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        labels = {
            "last_name": "Last Name",
            "first_name": "Last Name"
        }
        widgets = {
            "date_of_birth": DateInput()
        }
