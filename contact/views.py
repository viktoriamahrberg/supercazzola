from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    """
    View for contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



def contact_success(request):
    """
    View for Message sent successfully
    """
    messages.success(request, 'Your message was sent!')

    template = 'contact_success.html'
    return render(request, template)
