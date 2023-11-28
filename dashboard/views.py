from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'products': products,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):
    employees = User.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_view(request, primary_key):
    employee = User.objects.get(pk=primary_key)
    context = {
        'employee': employee,
    }
    return render(request, 'dashboard/staff_view.html', context)


@login_required
def product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'Product {product_name} has been added!')
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
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'dashboard/order.html', context)
