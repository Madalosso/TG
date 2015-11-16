from models import UsuarioFriends, Execution
from celery.utils.log import get_task_logger
from celery.decorators import task
import requests
import os
import time

logger = get_task_logger(__name__)


@task(name="RunExperiment")
def RunExperiment(execution, ide):
    print("\n Executando o exp %s, algoritmo: %s" % (ide, execution))
    os.system("mkdir " + str(ide))
    os.system("wget http://10.1.4.28:8000/experiments/downloadInputFile?id=" +
              str(ide) + " -O ./" + str(ide) + "/input")
    os.system(execution + " " + str(ide) + "/input >" + str(ide) + "/output")
    print (str("/"+str(ide) + "/output"))
    files={'file': str("/"+str(ide) + "/output")}
    r = requests.post('http://10.1.4.28:8000/experiments/result', files=files)
    print (r.status_code, r.reason)
           # execution.status = 2
           # execution.save()
           # start = time.time()
           # os.system(query)
           # dur = time.time() - start
           # print dur
           # execution.status = 3
           # user = execution.request_by
           # user.notes.add(nota)
           # user.save()
           # execution.time = dur
           # execution.outputFile = queryOutputFile
           # execution.save()

           # @task(name="RunExperiment")
           # def RunExperiment(query, execution, queryOutputFile):
           # print("\n Executando a query: %s" % (query))
           #     execution.status = 2
           #     execution.save()
           #     start = time.time()
           #     os.system(query)
           #     dur = time.time() - start
           #     print dur
           #     execution.status = 3
           #     user = execution.request_by
           # user.notes.add(nota)
           #     user.save()
           #     execution.time = dur
           #     execution.outputFile = queryOutputFile
           #     execution.save()
