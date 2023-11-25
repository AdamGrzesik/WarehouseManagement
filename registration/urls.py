from django.conf.urls.static import static
from django.urls import path
from warehouseProject import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-user'),
    path('profile/', views.profile, name='user-profile'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout-user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
