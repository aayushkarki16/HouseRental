from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class OwnerDetail(models.Model):
    user_name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    password1 = models.CharField(max_length=200, default='')


class HouseDetail(models.Model):
    user = models.CharField(max_length=200, default='   ')
    contact_person = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    mobile = models.CharField(max_length=200, default='')
    rent_type = models.CharField(max_length=200, default='')
    room_number = models.CharField(max_length=200, default='')
    client_type_a = models.CharField(max_length=200, default='')
    client_type = models.CharField(max_length=1000, default='')
    more_details = models.CharField(max_length=500, default='')
    monthly_price = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='image', default='')


class ClientCheck(models.Model):
    client = models.CharField(max_length=200, default='')



