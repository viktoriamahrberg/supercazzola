from django.shortcuts import render, redirect, reverse 
from django.contrib import messages 

from .forms import OrderForm


def checkout(request):
    """
    Checkout view
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, f'There is nothing in your cart at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        "order_form": order_form,
        "stripe_public_key": 'pk_test_51KyxvyLNFtsCYMEimXs9KJLHxA0e5WIIik7y1X17I8jUgLw8EPTGhvlU3zUmzNCnwpdJxNyR8ujN5lcqY8uqiamv00AHnK5FGJ',
        "client_secret": 'sk_test_51KyxvyLNFtsCYMEisyJtBzWxbVOI3WqLAbgBuIVyQK5Sk8Ow5wuDfYKQyTZWySSxDOZNsLOjbogc4JdOVqG8D8DH00kzbM3yw9',
    }

    return render(request, template, context)