from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import chain
from functools import reduce
import operator
from django.db.models import Avg

from .models import Product, Image, Color, Flower, ProductReview

from .forms import ProductForm, ProductReviewForm


def filter_product(request):
    # Product Filter
    categories = list(set(Product.objects.values_list('category', flat=True)))
    occasions = list(set(Product.objects.values_list('occasion', flat=True)))
    colors = list(set(Color.objects.all().values_list('name', flat=True)))
    flowers = list(set(Flower.objects.all().values_list('name', flat=True)))

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
        filtered_color = Color.objects.all().filter(reduce(operator.__or__,
                                              [Q(name__icontains=color) for color in color_name]))
        color_product_id = filtered_color.prefetch_related(
            'image_id').values_list('image_id__product_id', flat=True).distinct()
        if len(result_product_pk) > 0:
            result_product_pk = result_product_pk & set(color_product_id)
        else:
            result_product_pk = set(color_product_id)

    if len(flower_name) > 0:
        filtered_flower = Flower.objects.all().filter(reduce(operator.__or__,
                                                [Q(name__icontains=flower) for flower in flower_name]))
        flower_product_id = filtered_flower.values_list(
            'product_id', flat=True).distinct()
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

    product_list = Product.objects.filter(pk__in=result_product_pk)

    # Pagination
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'occasions': occasions,
        'colors': colors,
        'flowers': flowers,
        'products': products,
        'category_name': category_name,
        'color_name': color_name,
        'flower_name': flower_name,
        'occasion_name': occasion_name,
    }

    return render(request, 'products/products_onlineshop.html', context)


def onlineshop(request):
    """ A view for online shop (fintered with 'bouquet' category) """

    categories = list(set(Product.objects.values_list('category', flat=True)))
    occasions = list(set(Product.objects.values_list('occasion', flat=True)))
    colors = Color.objects.all()
    flowers = Flower.objects.all()
    product_list = Product.objects.all()

    category_name = ['bouquet']
    product_list = product_list.filter(category='bouquet')

    # Pagination
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'occasions': occasions,
        'colors': colors,
        'flowers': flowers,
        'products': products,
        'category_name': category_name,
    }

    return render(request, 'products/products_onlineshop.html', context)


def single_product(request, product_pk):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_pk)
    images = Image.objects.filter(product_id_id=product_pk)
    colors = Image.objects.prefetch_related(
        "color_set").filter(product_id_id=product_pk)

    if request.method == 'POST':
        product_review_form = ProductReviewForm(data=request.POST)
        if product_review_form.is_valid():
            # Create Review object but don't save to database yet
            new_review = product_review_form.save(commit=False)
            # Assign the current review to the product
            new_review.product_id = product
            # Save the review to the database
            new_review.save()
            product_review_form = ProductReviewForm()
            messages.success(request, 'Successfully posted your review.')
    else:
        product_review_form = ProductReviewForm()

    product_reviews = ProductReview.objects.filter(product_id_id=product_pk)

    if product_reviews:
        average_score = round(product_reviews.all().aggregate(Avg('rating_score'))['rating_score__avg'], 2)
        average_score_percentage = average_score/5*100
    else:
        average_score = "-"
        average_score_percentage = 0

    context = {
        'product': product,
        'colors': colors,
        'images': images,
        'product_reviews': product_reviews,
        'product_review_form': product_review_form,
        'average_score': average_score,
        'average_score_percentage': average_score_percentage,
    }

    return render(request, 'products/single_product.html', context)


@login_required
def delete_review(request, review_pk):
    """Delete a review posted by the user"""
    review = get_object_or_404(ProductReview, pk=review_pk)
    product_pk = review.product_id.pk
    review.delete()
    messages.success(request,
                     'Succesfully deleted your review.')
    return redirect(single_product, product_pk)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'You added the product successfully!')
            return redirect(reverse('single_product', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add the product. Please ensure the form is valid.')
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_pk):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'You updated {product.name}!')
            return redirect(reverse('single_product', args=[product_pk]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')

    else:
        form = ProductForm(instance=product)
        messages.info(
            request, f'You are editing a product details: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_pk):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_pk)
    product.delete()
    messages.success(request,
                     f'You deleted product: {product.name} from the database.')
    return redirect(reverse('onlineshop'))


def search_result(request):
    """A view to render the results by keyword search"""

    products = Product.objects.all()
    colors = Color.objects.all()
    flowers = Flower.objects.all()
    categories = list(set(Product.objects.values_list('category', flat=True)))
    occasions = list(set(Product.objects.values_list('occasion', flat=True)))
    queries = None

    if request.GET['q']:
        queries = request.GET['q'].split()

        filtered_colors = colors.filter(
            reduce(operator.__or__,
                   [Q(name__icontains=query) for query in queries]))
        filtered_flowers = flowers.filter(
            reduce(operator.__or__,
                   [Q(name__icontains=query) for query in queries]))
        filtered_products_name = products.filter(reduce(operator.__or__,
        [Q(name__icontains=query) | Q(description__icontains=query) for query in queries]))

        # Getting pk of product table from all the filters
        products_product_id = filtered_products_name.values_list(
            'pk', flat=True)
        flower_product_id = filtered_flowers.values_list(
            'product_id', flat=True).distinct()
        colors_product_id = filtered_colors.prefetch_related(
            'image_id').values_list('image_id__product_id', flat=True).distinct()

        result_product_pk = list(
            set(chain(products_product_id, flower_product_id)) - set(colors_product_id))

        products = Product.objects.filter(pk__in=result_product_pk)

    # Pagination
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'colors': colors,
        'flowers': flowers,
        'categories': categories,
        'occasions': occasions,
        'queries': queries,
    }

    return render(request, 'products/products_onlineshop.html', context)
