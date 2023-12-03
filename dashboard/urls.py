from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/view/<int:primary_key>/', views.staff_view, name='dashboard-staff-view'),
    path('products/', views.product, name='dashboard-product'),
    path('products/delete/<int:primary_key>/', views.product_delete, name='dashboard-product-delete'),
    path('products/edit/<int:primary_key>/', views.product_update, name='dashboard-product-update'),
    path('orders/', views.order, name='dashboard-order'),
    # CSV export
    path('orders/csv', views.export_orders_to_csv, name='export-orders-to-csv'),
    path('products/csv', views.export_products_to_csv, name='export-products-to-csv'),
]
