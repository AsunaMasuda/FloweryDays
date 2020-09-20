from django.shortcuts import render, redirect, reverse, HttpResponse,get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
    else:
        quantity = 1

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)