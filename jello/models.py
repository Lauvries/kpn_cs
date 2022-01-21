from wsgiref.validate import validator
from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    GENDER_OPTIONS = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    house_number = models.CharField(max_length=10)
    house_number_suffix = models.CharField(max_length=10, blank=True)
    zipcode = models.CharField(max_length=6, validators=[RegexValidator(
        regex='\d{4}[a-zA-Z]{2}', message="Please enter a zipcode like: 1234AB or 1234ab", code='invalid_zipcode')])
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, validators=[RegexValidator(
        regex='^06\d{8}', message="Please enter a phonenumber like 0612345678", code="invalid_phonenumber")])
    email = models.EmailField()
    products = models.ManyToManyField(
        "Product", related_name="customers", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Productname = {self.name}"
