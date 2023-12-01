from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Clothing', 'Clothing'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Health and Beauty', 'Health and Beauty'),
    ('Office', 'Office'),
    ('Sports and Outdoors', 'Sports and Outdoors'),
    ('Tools', 'Tools'),
    ('Toys and Games', 'Toys and Games'),
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


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Message(SingletonModel):
    text = models.CharField(max_length=300, default="Remember to complete your profile info!", null=False)

    class Meta:
        verbose_name_plural = 'Message'

    def __str__(self):
        return self.text
