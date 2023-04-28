from django.db import models

# Create your models here.
class FormData(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    country = models.CharField(max_length=8)
    state_or_district = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=4)
    phone_number1 = models.CharField(max_length=10)
    phone_number2 = models.CharField(max_length=10)
    email = models.CharField(max_length=255)

