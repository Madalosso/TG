from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from experiment.forms import ExecutionForm, ContactForm
from experiment.models import Execution, UsuarioFriends, Algorithms
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

@csrf_protect
def experiments(request):
    if request.method == 'POST':
        print request.POST
        opt = request.POST.get('opt')
        algorithm = request.POST.get('Algorithm')
        d_User = User.objects.get(username=request.user)
        alg = Algorithms.objects.get(nameAlg=algorithm)
        execution = Execution(
                request_by=d_User.usuariofriends,
                #     status=form.cleaned_data.get("status"),
                algorithm=alg,
                opt=opt #very tenso
            )
        execution.save()

        query = alg.command
        print(query)
        os.system(query)
        resp={}
        resp['resposta'] = 'FEXAMOS'
        return render(request, "experiments.html", resp)
    else:
        form = ExecutionForm(request.POST or None)  # request POST?
        if form.is_valid():
            d_User = User.objects.get(username=request.user)
            execution = Execution(
                request_by=d_User.usuariofriends,
                #     status=form.cleaned_data.get("status"),
                algorithm=form.cleaned_data.get("Algorithm"),
                opt=form.cleaned_data.get("opt") #very tenso
            )
            execution.save()
            
            # aqui deve ser feita a call pra executar o algoritmo
            alg = Algorithms.objects.get(nameAlg=form.cleaned_data.get("Algorithm"))
            query = alg.command
            print(query)
            os.system(query)
            resp={}
            resp['resposta'] = 'FEXAMOS'
            return render(request, "experiments.html", resp)

        title = "Experiments %s" % (request.user)
        context = {
            "title": title,
            "form": form
        }
        return render(request, "experiments.html", context)
