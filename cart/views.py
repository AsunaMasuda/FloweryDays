from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product, Image, Color


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    color = None

    if 'color' in request.POST:
        color = request.POST['color']
    cart = request.session.get('cart', {})

    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
    else:
        quantity = 1

    if color:
        if item_id in list(cart.keys()):
            if color in cart[item_id]['items_by_color'].keys():
                cart[item_id]['items_by_color'][color] += quantity
                messages.success(request, f'Updated quantity to \
                                 {cart[item_id]["items_by_color"][color]} for \
                                 {product.name} / color:{color.upper()}')
            else:
                cart[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Added {product.name} / \
                                 color: {color} to your bag')
        else:
            cart[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'Added {product.name} / \
                             color: {color} to your bag')
        # Get the image for toast when the product has a color choice
        images = Image.objects.all()
        colors = Color.objects.all()
        product_by_image = images.filter(product_id=product)
        product_by_color = colors.filter(name=color)
        result_image_pk = list(set(product_by_image.values_list('pk'))
                               .intersection(product_by_color
                               .values_list('image_id')))
        result_image = get_object_or_404(Image, pk=result_image_pk[0][0])

        request.session['last_item'] = {'name': product.name,
                                        'image': result_image.URL}

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} \
                             quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
        # Get the image for toast when the product does not have a color choice
        request.session['last_item'] = {'name': product.name,
                                        'image': product.product_image.url}

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Update the quantity of the selected product in the cart
        to a specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    messages.success(request, f"You've updated {product.name} \
                     quantity to {cart[item_id]}.")

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
        messages.success(request, f"You've removed \
                         {product.name} from your cart")

        request.session['cart'] = cart
        request.session['last_item'] = {'name': product.name,
                                        'image': image.filter(category='bouquet').filter(category='bouquet')
                                        }
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error occured. When removing \
                       {product.name} from your cart')
        return HttpResponse(status=500)
