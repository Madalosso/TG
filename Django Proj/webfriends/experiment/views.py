from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from experiment.forms import ExecutionForm, ContactForm
from experiment.models import Execution, UsuarioFriends, Algorithms
import os


# registration custom imports
from registration.views import RegistrationView
from registration.models import RegistrationProfile

# jsonview - Crispy validation
from jsonview.decorators import json_view
from crispy_forms.utils import render_crispy_form
from crispy_forms.helper import FormHelper


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
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)


@json_view
@csrf_protect
def checkForm(request):
    form = ExecutionForm(request.POST or None)  # request POST?
    print(request.POST)
    print "\n\n\n\n"
    if form.is_valid():  # processa
        experiments(request)
        helper = FormHelper()
        helper.form_id = 'form_exec'
        helper.form_action = '.'
        form_html = render_crispy_form(ExecutionForm(None), helper)
        return {'success': True, 'form_html': form_html}
        # exp = experiments(request)
        # form2 = ExecutionForm(request.POST or None)
        # return {'success': True, 'form_html': form2}
    else:
        helper = FormHelper()
        helper.form_id = 'form_exec'
        helper.form_action = '.'
        form_html = render_crispy_form(form, helper, RequestContext(request))
        return {'success': False, 'form_html': form_html}
        # return render(request, "experiments.html", {'success': False,
        # 'form_html': form_html})


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
            opt=opt,  # very tenso
        )
        execution.save()
        query = alg.command
        print(query)
        os.system(query)
        cont = {}
        cont['success'] = True
        cont['form_html'] = ExecutionForm(request.POST or None)
        return
        # return cont
        # return render(request, "experiments.html", cont)
    form = ExecutionForm(request.POST or None)
    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }
    return render(request, "experiments.html", context)
