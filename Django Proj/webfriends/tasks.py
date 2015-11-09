from celery import Celery
import os
import time
from models import UsuarioFriends, Execution

#broker =  user:pw@ip/vhost
#lsc5
experiment = Celery('tasks', backend='amqp',
                      broker='amqp://otavio:123@10.1.4.27/host1')

@experiment.task
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
    # user.notes.add(nota)
    user.save()
    execution.time = dur
    execution.outputFile = queryOutputFile
    execution.save()


@experiment.task(time_limit=17)
def teste():
    start = time.time()
    print start
    os.system("sleep 15")
    dur = time.time() - start
    print dur

@experiment.task
def add(n1,n2):
	return n1+n2
