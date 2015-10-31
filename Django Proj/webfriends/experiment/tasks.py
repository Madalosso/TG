from celery.decorators import task
from models import Note, UsuarioFriends, Execution
import os


@task()
def RunExperiment(query, execution, queryOutputFile):
    print("\n Executando a query: %s" % (query))
    execution.status = 2
    execution.save()
    os.system(query)
    execution.status = 3
    nota = Note(execution=execution, user=execution.request_by, noteType=1)
    user = execution.request_by
    nota.save()
    user.notes.add(nota)
    user.save()
    execution.outputFile = queryOutputFile
    execution.save()


@task(time_limit=10)
def teste():
    os.system("sleep 15")
