from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, primary_key):
    product_to_delete = Product.objects.get(pk=primary_key)
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect('dashboard-product')
    context = {
        'product_to_delete': product_to_delete,
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required
def product_update(request, primary_key):
    product_to_update = Product.objects.get(pk=primary_key)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product_to_update)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=product_to_update)
    context = {
        'product_to_update': product_to_update,
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    return render(request, 'dashboard/order.html')
