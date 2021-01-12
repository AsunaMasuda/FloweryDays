from django.test import TestCase
from products.models import Product, Image, Color, Flower, ProductReview
from django.contrib.auth.models import User


class TestProductModel(TestCase):

    def test_product(self):
        product = Product(name='product_name')
        self.assertEqual(str(product), 'name: product_name')


class TestImageModel(TestCase):

    def test_product_image(self):
        product = Product(name='product_name',
                          category='test_category',
                          price=30,
                          occasion='test_occasion',
                          description='test_description')
        product.save()
        product_image = Image(name='product_image', product_id=product)
        self.assertEqual(str(product_image),
                         'product_image, name: product_name')


class TestColorModel(TestCase):

    def test_product_color(self):
        color = Color(name='test_color')
        self.assertEqual(str(color), 'test_color')


class TestFlowerModel(TestCase):

    def test_product_flower(self):
        flower = Flower(name='test_color')
        self.assertEqual(str(flower), 'test_color')


class TestProductReviewModel(TestCase):

    def test_product_review(self):

        user = User(username='testuser')
        user.save()
        product_review = ProductReview(user_id=user,
                                       review_title='review_title_test',
                                       rating_score=int(5))
        self.assertEqual(product_review.review_rate, 100)
        self.assertEqual(str(product_review),
                         'user: testuser, review_title: review_title_test')
