from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    occasion = models.CharField(max_length=30)
    description = models.TextField()
    unit = models.CharField(max_length=30, null=False, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    product_image = models.ImageField(null=False, blank=True)

    def __str__(self):
        return 'name: {}'.format(self.name)


class Image(models.Model):
    name = models.CharField(max_length=254, null=False, blank=True)
    image = models.ImageField(null=False, blank=False)
    URL = models.URLField(max_length=1024, null=False, blank=True)
    product_id = models.ForeignKey('Product', null=True,
                                   blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}, {}'.format(self.name, self.product_id)


class Color(models.Model):
    name = models.CharField(max_length=254)
    image_id = models.ManyToManyField('Image')

    def __str__(self):
        return '{}'.format(self.name)


class Flower(models.Model):
    name = models.CharField(max_length=254)
    product_id = models.ManyToManyField('Product')

    def __str__(self):
        return '{}'.format(self.name)


class ProductReview(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product_id = models.ForeignKey('Product', null=True,
                                   blank=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True,
                                blank=True, on_delete=models.SET_NULL)
    rating_score = models.IntegerField(choices=RATING_CHOICES, default=0)
    review_title = models.CharField(max_length=254)
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='review_created_date')

    @property
    def review_rate(self):
        return self.rating_score/5*100

    def __str__(self):
        return 'user: {}, review_title: {}'.format(self.user_id,
                                                      self.review_title)
