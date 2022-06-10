from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    """
    View for contact form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject, message, from_email, ['hello@supercazzola.com']
                    )
            except BadHeaderError:
                messages.error(request, (
                        "Invalid header found.")
                    )
            return redirect('contact_success')
    return render(request, "contact.html", {'form': form})


def contact_success(request):
    """
    View for Message sent successfully
    """
    messages.success(request, 'Your message was sent!')

    template = 'contact_success.html'
    return render(request, template)
