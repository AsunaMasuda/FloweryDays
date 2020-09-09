from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from functools import reduce
import operator

from .models import Product, Image, Color, Flower


def filter_product(request):
    categories = list(set(Product.objects.values_list('category', flat=True)))
    occasions = list(set(Product.objects.values_list('occasion', flat=True)))
    colors = Color.objects.all()
    flowers = Flower.objects.all()

    category_name = request.GET.getlist('filter_category')
    color_name = request.GET.getlist('filter_color')
    flower_name = request.GET.getlist('filter_flower')
    occasion_name = request.GET.getlist('filter_occasion')

    result_product_pk = set()

    if len(category_name) > 0:
        filtered_category = Product.objects.all().filter(reduce(operator.__or__,
            [Q(category__icontains=category) for category in category_name]))
        category_product_id = filtered_category.values_list('pk', flat=True)
        result_product_pk = set(category_product_id)

    if len(color_name) > 0:
        filtered_color = colors.filter(reduce(operator.__or__,
            [Q(name__icontains=color) for color in color_name]))
        color_product_id = filtered_color.prefetch_related('image_id').values_list('image_id__product_id', flat=True).distinct()
        if len(result_product_pk) > 0:
            result_product_pk = result_product_pk & set(color_product_id)
        else: 
            result_product_pk = set(color_product_id)

    if len(flower_name) > 0:
        filtered_flower = flowers.filter(reduce(operator.__or__,
            [Q(name__icontains=flower) for flower in flower_name]))
        flower_product_id = filtered_flower.values_list('product_id', flat=True).distinct()
        if len(result_product_pk) > 0:
            result_product_pk = result_product_pk & set(flower_product_id)
        else: 
            result_product_pk = set(flower_product_id)

    if len(occasion_name) > 0:
        filtered_occasion = Product.objects.all().filter(reduce(operator.__or__,
            [Q(occasion__icontains=occasion) for occasion in occasion_name]))
        occasion_product_id = filtered_occasion.values_list('pk', flat=True)
        if len(result_product_pk) > 0:
            result_product_pk = result_product_pk & set(occasion_product_id)
        else: 
            result_product_pk = set(occasion_product_id)

    products = Product.objects.filter(pk__in=result_product_pk)

    context = {
        'categories': categories,
        'occasions': occasions,
        'colors': colors,
        'flowers': flowers,
        'products': products,
    }

    return render(request, 'products/products_onlineshop.html', context)
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