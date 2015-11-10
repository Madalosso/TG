from celery.decorators import task
from models import UsuarioFriends, Execution
import os
import time


@task(time_limit=900)
def RunExperiment(query, execution, queryOutputFile):
    # print("\n Executando a query: %s" % (query))
    execution.status = 2
    execution.save()
    start = time.time()
    os.system(query)
    dur = time.time() - start
    print dur
    execution.status = 3
    user = execution.request_by
    #user.notes.add(nota)
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
