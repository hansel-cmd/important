from django.contrib import admin

from .models import User, UserDetail, Coffee

# Register your models here.
admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(Coffee)
