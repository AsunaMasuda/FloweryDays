from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Image, Color


def cart_contents(request):
    """ Enables the cart content available across the whole website """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    last_item = request.session.get('last_item', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for color, quantity in item_data['items_by_color'].items():
                total += quantity * product.price
                product_count += quantity
                # Get the image when the product has a color choice
                images = Image.objects.all()
                colors = Color.objects.all()
                product_by_image = images.filter(product_id=product)
                product_by_color = colors.filter(name=color)
                result_image_pk = list(set(product_by_image.values_list('pk'))
                                       .intersection(product_by_color
                                       .values_list('image_id')))
                product_image = get_object_or_404(Image,
                                                  pk=result_image_pk[0][0])

                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'color': color,
                    'product_image': product_image.URL,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    last_added_item = last_item

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'last_added_item': last_added_item,
    }

    return context
