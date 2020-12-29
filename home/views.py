from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError

from django.conf import settings

from .forms import ContactForm


def index(request):
    """
    """
    template = 'home/index.html'
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
        name = contact_form['name']
        email = contact_form['email']
        subject = contact_form['subject']
        message = contact_form['message']
        try:
            send_mail(
                f"You've got a message from {name} ({email}) on contact form.",
                f"Subject: {subject}, Message: {message}",
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return redirect(thankyou_page)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')


def thankyou_page(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'home/thankyou_page.html')
