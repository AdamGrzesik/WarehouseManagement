from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/view/<int:primary_key>/', views.staff_view, name='dashboard-staff-view'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:primary_key>/', views.product_delete, name='dashboard-product-delete'),
    path('product/edit/<int:primary_key>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
]
