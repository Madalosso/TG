from celery import Celery

#broker =  user:pw@ip/vhost
#lsc5
experiment = Celery('tasks', backend='amqp',
                      broker='amqp://otavio:123@10.1.4.28/host1')

@experiment.task
def add(x, y):
     return x + y
