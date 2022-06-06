from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

from products.models import Product


def profile(request):
    """ 
    Renders user's profile account
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information has been updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
