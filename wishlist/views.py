from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import WishlistItem
from products.models import Product



@login_required
def add_to_wishlist(request, product_id):
    """
    Add product to My Wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlistitem = get_object_or_404(WishlistItem, user=request.user.id)
    except Http404:
        wishlistitem = WishlistItem.objects.create(user=request.user)
    else:
        wishlistitem.product.add(product)
        messages.info(request, f'{product.name} was added to My Wishlist.')
        return redirect(reverse('products'))


