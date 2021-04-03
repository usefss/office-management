from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


#     name = models.CharField(max_length=32, required=True)
#     phone_number = models.CharField(max_length=32, required=True)
#     email = models.CharField(max_length=32)
#
#
# class SearchDoctor(models.Model):
#     name = models.CharField(max_length=32, null=True)
#     city = models.CharField(max_length=32, null=True)
#     expertise = models.CharField(max_length=32, null=True)
#     degree = models.CharField(max_length=32, null=True)
#
#
# class PatientInfo(models.Model):
#     name = models.CharField(max_length=32)
#     phone_number = models.CharField(max_length=32)




