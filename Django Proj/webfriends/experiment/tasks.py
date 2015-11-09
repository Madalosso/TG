from __future__ import absolute_import

from celery import shared_task


@shared_task
def add1(x,y):
	return x+y

