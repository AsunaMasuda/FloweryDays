from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contexts

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is no item in your cart.")
        redirect(reverse('onlineshop'))

    current_cart = cart_contexts(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create {
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    }

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)