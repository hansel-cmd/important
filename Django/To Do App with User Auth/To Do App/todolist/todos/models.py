from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):

#     username = models.CharField(max_length=20,unique=True)
#     email = models.EmailField(max_length=20)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{type(self).__name__}(username = {self.username})"

class ToDo(models.Model):

    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{type(self).__name__}(title = {self.title}, is_completed = {self.is_completed})"
    
