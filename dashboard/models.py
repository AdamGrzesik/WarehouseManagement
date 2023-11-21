from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Office', 'Office'),
    ('Electronics', 'Electronics'),
    ('Miscellaneous', 'Miscellaneous'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}: {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}, requested by {self.staff}'
