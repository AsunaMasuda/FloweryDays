from django.shortcuts import render, redirect, reverse, HttpResponse,get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
    else:
        quantity = 1

    cart = request.session.get('cart', {})
    last_item = request.session.get('last_item', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"You've updated {product.name} quantity to {cart[item_id]}.")
    else:
        cart[item_id] = quantity
        messages.success(request, f"You've added {product.name} to your cart.")

    request.session['cart'] = cart
    request.session['last_item'] = {'name': product.name,
                                    'image': product.product_image.url}

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Update the quantity of the selected product in the cart
        to a specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    messages.success(request, 
    f"You've updated {product.name} quantity to {cart[item_id]}.")

    request.session['cart'] = cart
    request.session['last_item'] = {'name': product.name,
                                    'image': product.product_image.url}
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the specified item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f"You've removed {product.name} from your cart")

        request.session['cart'] = cart
        request.session['last_item'] = {'name': product.name,
                                        'image': product.product_image.url}
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error occured. When removing {product.name} from your cart')
        return HttpResponse(status=500)