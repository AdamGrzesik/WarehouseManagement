from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-user'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout-user'),
]
