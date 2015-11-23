from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from experiment.forms import ExecutionForm, ContactForm
from experiment.models import Execution, Algorithms, UsuarioFriends
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.core.files import File
# jsonview - Crispy validation
from jsonview.decorators import json_view
from crispy_forms.utils import render_crispy_form
from crispy_forms.helper import FormHelper

# paginator
from paginator import paginate

from experiment.tasks import RunExperiment

def about(request):
    return HttpResponse(1)


def home(request):
    if not request.user.is_authenticated():
        title = "Welcome"
        context = {
            "title": title
        }
        return render(request, "welcome.html", context)
    else:
        # res = teste.delay()
        # print res
        title = "Welcome %s" % request.user
        print(request.user.id)
        executionList = Execution.objects.filter(
            request_by__usuario__id=request.user.id).order_by('-id')
        try:
            UserProf = UsuarioFriends.objects.get(usuario__id=request.user.id)
        except:
            print "Erro. Criando novo userProf"
            user = User.objects.get(id=request.user.id)
            UserProf = UsuarioFriends(usuario=user)
            UserProf.save()
            print "Criado novo UserProf"
        paginator = Paginator(executionList, UserProf.resultsPerPage)
        page = request.GET.get('page')
        if page is None:
            page = 1
        try:
            executions = paginator.page(page)
        except PageNotAnInteger:
            executions = paginator.page(1)
        except EmptyPage:
            executions = paginator.page(paginator.num_pages)  # da pra tratar
        if paginator.count == 0:
            data = None
        else:
            data = executions
        pageI = paginate(page, paginator)
        context = {
            "title": title,
            "data": data,
            "pagesIndex": pageI,
        }
        return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


def downloadInputFile(request):
    expId = request.GET.get('id')
    execution = Execution.objects.get(pk=expId)
    # if (execution.request_by.usuario.id == request.user.id):
    #     response = HttpResponse(
    #         execution.inputFile, content_type='application/force-download')
    #     response[
    #         'Content-Disposition'] = 'attachment; filename="entrada-Experimento-' + str(expId) + '"'
    #     return response
    # criar alerta
    response = HttpResponse(
        execution.inputFile, content_type='application/force-download')
    response[
        'Content-Disposition'] = 'attachment; filename="entrada-Experimento-' + str(expId) + '"'
    return response
    # return HttpResponseRedirect(reverse('home'))


def downloadOutputFile(request):
    expId = request.GET.get('id')
    execution = Execution.objects.get(pk=expId)
    if (execution.request_by.usuario.id == request.user.id):
        print execution.outputFile.url
        print "Autorizado"
        response = HttpResponse(
            execution.outputFile, content_type='application/force-download')
        response[
            'Content-Disposition'] = 'attachment; filename="Resultado-Experimento-' + str(expId) + '"'
        return response
    print "Nao autorizado"
    # criar alerta
    return HttpResponseRedirect(reverse('home'))


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


# ajax


@json_view
@csrf_protect
def checkForm(request):
    form = ExecutionForm(request.POST or None)  # request POST?
    print(request.POST)
    print "\n\n"
    if form.is_valid():  # processa
        experiments(request)
        helper = FormHelper()
        helper.form_id = 'form_exec'
        helper.form_action = '.'
        form_html = render_crispy_form(ExecutionForm(None), helper)
        return {'success': True, 'form_html': form_html}
    else:
        helper = FormHelper()
        helper.form_id = 'form_exec'
        helper.form_action = '.'
        form_html = render_crispy_form(form, helper, RequestContext(request))
        return {'success': False, 'form_html': form_html}


@csrf_protect
def experiments(request):
    if request.method == 'POST':
        form = ExecutionForm(request.POST, request.FILES or None)
        if not form.is_valid():
            title = "Experiments %s" % (request.user)
            # form_html = render_crispy_form(form)
            context = {
                "form": form,
                'title': title
            }
            return render(request, "experiments.html", context)
        algorithm = request.POST.get('Algorithm')
        d_User = User.objects.get(username=request.user)
        alg = Algorithms.objects.get(nameAlg=algorithm)
        execution = Execution(
            request_by=d_User.usuariofriends,
            algorithm=alg,
        )
        execution.save()
        if (request.FILES):
            # print request.FILES
            fileIn = request.FILES["Input"]
            execution.inputFile = fileIn
            execution.save()
            queryInputFile = (
                settings.MEDIA_ROOT +
                execution.inputFile.name.replace('./', '/')
            ).replace(' ', '\ ')
            queryOutputFile = queryInputFile
            queryOutputFile = queryOutputFile.replace('input', 'output')
            # print "QUERY OUT : " + queryOutputFile
            query = alg.command + ' ' + queryInputFile + '>' + queryOutputFile
            # print query
        else:
            query = execution.algorithm.command
        outputFilePath = './users/user_' + \
            str(execution.request_by.usuario.id) + \
            '/' + str(execution.id) + '/output'
        # print(outputFilePath)
        # teste = RunExperiment.delay(execution.algorithm.command)
        teste = RunExperiment.delay(alg.command, execution.id)
        # teste = RunExperiment.delay(query, execution, outputFilePath)
        #print teste.status
        # RunExperiment.apply_async(
        #     args=[query, execution, outputFilePath], kwargs={}, countdown=60)
        # RunExperiment.delay(query, execution, outputFilePath)
        # os.system(query)
        # execution.outputFile = queryOutputFile
        execution.save()
        title = "Experiments %s" % (request.user)
        # cont = {"title": title, "form": form}
        return HttpResponseRedirect(reverse('home'))
        # return render(request, "experiments.html", cont)
    form = ExecutionForm(request.POST or None)
    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }
    return render(request, "experiments.html", context)

def experimentsRemove(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data:
            ids = data.split(",")
            print ids
            Execution.objects.filter(id__in=ids).delete()
        # objects = Model.objects.filter(id__in=object_ids)
    return HttpResponseRedirect(reverse('home'))

@csrf_exempt
def result(request):
    print "testePRINT"
    if request.method == 'POST':
        print "POST"
        if (request.FILES):
	    idExec = request.POST.get("id")
	    tempo  = request.POST.get("time")
	    print idExec
	    print tempo
	    execution = Execution.objects.get(id=idExec)
	    fileIn = request.FILES["file"]
	    execution.outputFile=fileIn
	    execution.status=3
	    execution.time = tempo
            execution.save()
    return HttpResponse(1)
