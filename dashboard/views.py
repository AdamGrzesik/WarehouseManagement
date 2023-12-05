from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Message
from .forms import ProductForm, OrderForm, OrderUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
import csv


# Create your views here.
@login_required
def index(request):
    counts = {
        'products_count': Product.objects.all().count(),
        'orders_count': Order.objects.all().count(),
        'employees_count': User.objects.filter(is_staff=True).count(),
    }

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
        'message': Message.load().text,
    }
    return render(request, 'dashboard/index.html', context | counts)


@login_required
def staff(request):
    employees = User.objects.all()
    employees_count = employees.count()
    context = {
        'employees': employees,
        'employees_count': employees_count,
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
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-order')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, 'dashboard/order.html', context)


@login_required
def order_update(request, primary_key):
    order_to_update = Order.objects.get(pk=primary_key)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance=order_to_update)
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
        form = OrderUpdateForm(instance=order_to_update)
    context = {
        'order_to_update': order_to_update,
        'form': form,
    }
    return render(request, 'dashboard/order_update.html', context)


@login_required
def order_delete(request, primary_key):
    order_to_delete = Order.objects.get(pk=primary_key)
    if request.method == 'POST':
        order_to_delete.delete()
        return redirect('dashboard-order')
    context = {
        'order_to_delete': order_to_delete,
    }
    return render(request, 'dashboard/order_delete.html', context)


# CSV export
@login_required
def export_orders_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Product', 'Category', 'Quantity', 'Order by', 'Date'])

    if request.user.is_staff:
        orders = Order.objects.filter(status='Active').values_list('product__name', 'product__category', 'quantity',
                                                                   'staff__first_name', 'staff__last_name', 'date')
    else:
        orders = Order.objects.filter(staff=request.user, status='Active').values_list('product__name',
                                                                                       'product__category', 'quantity',
                                                                                       'staff__first_name',
                                                                                       'staff__last_name', 'date')
    for record in orders:
        order_by = ' '.join(record[3:5])
        record = record[:3] + (order_by,) + record[5:]
        writer.writerow(record)
    return response


@login_required
def export_products_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Name', 'Category', 'Quantity'])

    products = Product.objects.all().values_list('name', 'category', 'quantity')
    for record in products:
        writer.writerow(record)

    return response
