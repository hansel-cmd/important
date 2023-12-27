from django.contrib import admin

# Register your models here.
from .models import ToDo, User

admin.site.register(ToDo)
