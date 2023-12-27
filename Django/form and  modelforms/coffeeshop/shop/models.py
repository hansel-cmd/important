from django.db import models
from django.core.validators import MinLengthValidator

from .validators import vaidate_address
from .utils import *

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return f"{type(self).__name__}(username = {self.username}, password = {self.password})"
    

class UserDetail(models.Model):

    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(10)])
    zipcode = models.CharField(max_length=4)
    address = models.CharField(max_length=200, validators=[vaidate_address])

    def __str__(self):
        return (f"{type(self).__name__}(username = {self.username}, "
        "first_name = {self.first_name}, "
        "last_name = {self.last_name}, "
        "email = {self.email}, "
        "address = {self.address})"
        )
    
class Coffee(models.Model):

    name = models.CharField(max_length=10, choices=COFFEE_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    quantity = models.CharField(max_length=1, choices=QUANTITY_CHOICES)

    def __str__(self):
        return f"{type(self).__name__}(name = {self.name}, size = {self.size}, quantity = {self.quantity})"