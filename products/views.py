from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from functools import reduce
import operator

from .models import Product, Image, Color, Flower


def onlineshop(request):
    categories = list(set(Product.objects.values_list('category', flat=True)))
    occasions = list(set(Product.objects.values_list('occasion', flat=True)))
    colors = Color.objects.all()
    flowers = Flower.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'occasions': occasions,
        'colors': colors,
        'flowers': flowers,
        'products': products,
    }
    return render(request, 'products/products_onlineshop.html', context)


def single_product(request, product_pk):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_pk)
    images = Image.objects.filter(product_id_id=product_pk)
    colors = Image.objects.prefetch_related("color_set").filter(product_id_id=product_pk)

    context = {
        'product': product,
        'colors': colors,
        'images': images,
    }

    return render(request, 'products/single_product.html', context)


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    colors = Color.objects.all()
    flowers = Flower.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            queries = request.GET['q'].split()
            colors =  colors.filter(reduce(operator.__or__, [Q(name__icontains=query) for query in queries]))
            flowers =  flowers.filter(reduce(operator.__or__, [Q(name__icontains=query) for query in queries]))
            products =  products.filter(reduce(operator.__or__, [Q(name__icontains=query) | Q(description__icontains=query) for query in queries]))

            # QuerySet with images of a searched color
            color_filtered = colors.prefetch_related('image_id__product_id')

            # Getting pk of product table from all the filters
            products_product_id = products.values_list('pk', flat=True)
            flower_product_id = flowers.values_list('product_id', flat=True).distinct()
            colors_product_id = colors.prefetch_related('image_id').values_list('image_id__product_id', flat=True).distinct()

            result_product_pk = list(set(chain(products_product_id, flower_product_id)) - set(colors_product_id))

            filtered_product = Product.objects.filter(pk__in=result_product_pk)

    context = {
        'filtered_product': filtered_product,
        'color_filtered': color_filtered,
        'search_term': query,
    }

    return render(request, 'products/products_onlineshop.html', context)