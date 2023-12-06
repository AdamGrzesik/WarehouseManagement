from django.test import TestCase, Client
from django.urls import reverse


class DashboardIndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_index_url = reverse('dashboard-index')

    def test_dashboard_index_view_GET(self):
        response = self.client.get(self.dashboard_index_url)
        self.assertEqual(response.status_code, 302)


class DashboardStaffViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_staff_url = reverse('dashboard-staff')

    def test_dashboard_staff_view_GET(self):
        response = self.client.get(self.dashboard_staff_url)
        self.assertEqual(response.status_code, 302)


class DashboardProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_product_url = reverse('dashboard-product')

    def test_dashboard_product_view_GET(self):
        response = self.client.get(self.dashboard_product_url)
        self.assertEqual(response.status_code, 302)


class DashboardOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_order_url = reverse('dashboard-order')

    def test_dashboard_order_view_GET(self):
        response = self.client.get(self.dashboard_order_url)
        self.assertEqual(response.status_code, 302)


class DashboardOrderUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_order_update_url = reverse('dashboard-order-update', args=[1])

    def test_dashboard_order_update_view_GET(self):
        response = self.client.get(self.dashboard_order_update_url)
        self.assertEqual(response.status_code, 302)
