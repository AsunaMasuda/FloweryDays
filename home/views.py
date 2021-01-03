from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from profiles.models import UserProfile

from django.conf import settings

from .forms import ContactForm


def index(request):
    """
    Render index.html and ContactForm
    """
    template = 'home/index.html'

    # Prefill the email address field at contact form
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        contact_form = ContactForm(initial={"email": profile.default_email})
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)


def contactform(request):
    """
    Send an email to the admin
    when site visitors send message via contact form
    """
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        message = contact_form.cleaned_data['message']
        try:
            send_mail(
                f"You've got a message from {name} ({email}) on contact form.",
                f"Subject: {subject}, Message: {message}",
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return redirect('thankyou_page')


def thankyou_page(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'home/thankyou_page.html')
