# TCC
Trabalho de Conclusao de Curso
Requisitos:

Django 1.8 

Celery 3.1.18 pip install Celery

#Celery-Django pip install django-celery

django-registration-redux 1.2 http://django-registration-redux.readthedocs.org/en/latest/quickstart.html

django-crispy-forms   http://django-crispy-forms.readthedocs.org/en/1.1.1/install.html

django-jsonview   https://github.com/jsocol/django-jsonview

Broker Redis 3.0 http://redis.io/download

Requests 2.8.1 http://docs.python-requests.org/en/latest/user/install/#install

to start server: on Django Proj/webfriends/ "./manage.py runserver"

to start worker: on Django Proj/webfriends/ "celery -A webfriends worker -l info"

config broker on settings.py
set urls on experiments/tasks.py
