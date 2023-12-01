from django.contrib import admin
from .models import Product, Order, Message

admin.site.site_header = 'Warehouse Admin Dashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Message)
