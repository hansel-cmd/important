from django.db import models
from django.conf import settings
from decimal import Decimal

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=15, decimal_places=2, default=Decimal('99.99'))
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    public = models.BooleanField(default=True)

    @property
    def sale_price(self):
        return "{:.2f}".format(float(self.price) * 0.8)

    def __str__(self):
        return f"${type(self).__name__}(pk = {self.pk}, title = {self.title}, content = {self.content}, price = {self.price})"
