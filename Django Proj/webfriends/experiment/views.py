from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from experiment.forms import ExecutionForm, ContactForm
from experiment.models import Execution,UsuarioFriends
import os


# registration custom imports
from registration.views import RegistrationView
from registration.models import RegistrationProfile

# Django Ajax
#from django_ajax.decorators import ajax

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
        subject = 'Portal Friends - Mensagem de %s ' % (
            form.cleaned_data.get("nome"))
        from_email = settings.EMAIL_HOST_USER  # da pra usar outro?
        to_email = from_email
        message = form.cleaned_data.get("mensagem")
        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=False)
        # for key in form.cleaned_data:
            # print form.cleaned_data.get(key)
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)


def experiments(request):
    form = ExecutionForm(request.POST or None)  # request POST?
    if form.is_valid():
        d_User = User.objects.get(username=request.user)
        execution = Execution(
            request_by=d_User.usuariofriends, status=form.cleaned_data.get("status"))
        execution.save()
        #aqui deve ser feita a call pra executar o algoritmo
        #os.system('./script.sh')
    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }
    return render(request, "experiments.html", context)
