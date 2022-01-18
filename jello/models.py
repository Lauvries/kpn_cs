from re import M
from django.db import models


class Customer(models.Model):
    GENDER_OPTIONS = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]

    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    house_number = models.IntegerField()
    house_number_suffix = models.CharField(max_length=10, blank=True)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
