from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """A template tag to calculate multiple price by quantity"""

    return price * quantity
