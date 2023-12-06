from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register-user')

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_view_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 200)


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login-user')

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout-user')

    def test_logout_view_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logout.html')


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('user-profile')
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_view_GET(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')


class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_update_url = reverse('user-profile-update')
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_update_view_GET(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.profile_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile_update.html')

    def test_profile_update_view_POST(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(self.profile_update_url, {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
        })
        self.assertEqual(response.status_code, 200)
