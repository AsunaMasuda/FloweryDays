from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    occasion = models.CharField(max_length=30)
    description = models.TextField()
    unit = models.CharField(max_length=30, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    URL = models.URLField(max_length=1024, null=True, blank=True)
    product_id = models.ForeignKey('Product', null=True,
                                   blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=254)
    image_id = models.ManyToManyField('Image')

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=254)
    product_id = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
