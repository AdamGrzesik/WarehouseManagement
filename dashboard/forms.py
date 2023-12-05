from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product'].choices = [(product.id, product.name) for product in Product.objects.all()]


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'status']
