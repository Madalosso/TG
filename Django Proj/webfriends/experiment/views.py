from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import os


#registration custom imports
from registration.views import RegistrationView
from registration.models import RegistrationProfile


# Create your views here.


def home(request):
    title = "Home %s" % (request.user)
    context = {
        "title": title
    }
    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = 'TESTE'
        from_email = settings.EMAIL_HOST_USER
        to_email = from_email
        message = form.cleaned_data.get("message")
        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=False)
        # for key in form.cleaned_data:
            #print form.cleaned_data.get(key)
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)

def experiments(request):
    title = "Experiments %s" % (request.user)
    context = {
        "title": title
    }
    return render(request, "experiments.html", context)