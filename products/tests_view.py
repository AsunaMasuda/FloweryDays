from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product


class TestProductView(TestCase):
    """
    Tests for views renders templates in pruduct app
    """
    def setUp(self):
        # Create author
        User.objects.create_superuser('superuser',
                                      'superuser@test.com',
                                      'superuserpassword')

        self.product = Product(name='test_name',
                               category='test_category',
                               price=10,
                               occasion='test_occasion',
                               description='test_description',
                               unit='1 bunch')
        self.product.save()

    def test_onlineshop(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products_onlineshop.html')

    def test_filter(self):
        response = self.client.get('/products/filter_result/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products_onlineshop.html')

    def test_add_product(self):
        self.client.login(username='superuser', password='superuserpassword')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_delete_product(self):
        self.client.login(username='superuser', password='superuserpassword')
        response = self.client.get('/products/delete/{0}/'
                                   .format(self.product.pk))
        self.assertRedirects(response, '/products/',
                             status_code=302, target_status_code=200,
                             fetch_redirect_response=True)
