from celery.decorators import task
from models import Note, UsuarioFriends, Execution
import os
import time


@task()
def RunExperiment(query, execution, queryOutputFile):
    # print("\n Executando a query: %s" % (query))
    execution.status = 2
    execution.save()
    start = time.time()
    os.system(query)
    dur = time.time() - start
    print dur
    execution.status = 3
    nota = Note(execution=execution, user=execution.request_by, noteType=1)
    user = execution.request_by
    nota.save()
    user.notes.add(nota)
    user.save()
    execution.time = dur
    execution.outputFile = queryOutputFile
    execution.save()


@task(time_limit=17)
def teste():
    start = time.time()
    print start
    os.system("sleep 15")
    dur = time.time() - start
    print dur
