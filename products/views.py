from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from itertools import chain

from .models import Product, Image, Color, Flower


def initial_products(request):
    return render(request, 'products/products_onlineshop.html')


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    colors = Color.objects.all()
    flowers = Flower.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            colors = colors.filter(Q(name__icontains=query))
            flowers = flowers.filter(Q(name__icontains=query))
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

            products_product_id = products.values_list('pk', flat=True)
            colors_product_id = colors.prefetch_related('image_id').values_list('image_id__product_id', flat=True).distinct()
            flower_product_id = flowers.values_list('product_id', flat=True).distinct()
            result_product_pk = list(set(chain(products_product_id, colors_product_id, flower_product_id)))

            product_result = Product.objects.filter(pk__in=result_product_pk)

    context = {
        'products': product_result,
        'search_term': query,
    }

    return render(request, 'products/products_onlineshop.html', context)