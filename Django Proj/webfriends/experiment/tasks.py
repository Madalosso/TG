from celery.decorators import task
# from models import Execution
import os


@task()
def RunExperiment(query, execution, queryOutputFile):
    print("\n Executando a query: %s" % (query))
    execution.status = 2
    execution.save()
    os.system(query)
    execution.status = 3
    execution.outputFile = queryOutputFile
    execution.save()


@task()
def teste():
    os.system("sleep 15")
