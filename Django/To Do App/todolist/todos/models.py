from django.db import models

# Create your models here.
class ToDo(models.Model):

    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default = False)

    def __str__(self):
        return f"{type(self).__name__}(title = {self.title}, is_completed = {self.is_completed})"