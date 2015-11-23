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
    start = time.time()
    os.system(execution + " " + str(ide) + "/input >" + str(ide) + "/output")
    dur = time.time() - start
    
    print dur
    files={'file': str("/"+str(ide) + "/output")}
    path = str(str(ide)+"/output")
    print path
    files = {'file': open(path, 'rb')}
    data = {'id':str(ide),'time':dur}
    #   r = requests.post('http://10.1.4.28:8000/about/')
    r = requests.post('http://10.1.4.28:8000/experiments/result', files=files,data=data)
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
