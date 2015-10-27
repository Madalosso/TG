from celery import Celery

experiment = Celery('tasks', backend='amqp',
                      broker='amqp://guest:guest@localhost:5672//')

@experiment.task
def add(x, y):
     return x + y